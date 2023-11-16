import csv
import os
from pathlib import Path
from typing import Iterable, Optional, Union


import fiona
import rasterstats

from eedl.core import safe_fiona_open


def zonal_stats(features: Union[str, Path, fiona.Collection],
				raster: Union[str, Path, None],
				output_folder: Union[str, Path, None],
				filename: str,
				keep_fields: Iterable[str] = ("UniqueID", "CLASS2"),
				stats: Iterable[str] = ('min', 'max', 'mean', 'median', 'std', 'count', 'percentile_10', 'percentile_90'),
				report_threshold: int = 1000,
				write_batch_size: int = 2000,
				use_points: bool = False,
				inject_constants: dict = dict(),
				nodata_value: int = -9999,
				**kwargs) -> Union[str, Path, None]:
	# TODO: Make this check if raster and polys are in the same CRS - if they're not, then rasterstats doesn't
	#  automatically align them and we just get bad output.

	"""
	If the raster and the polygons are not in the CRS, this function will produce bad output.

	:param features: Location to the features.
	:type features: Union[str, Path, fiona.Collection]
	:param raster: Location of the raster.
	:type raster: Union[str, Path, None]
	:param output_folder: Output destination.
	:type output_folder: Union[str, Path, None]
	:param filename: Name of the file.
	:type filename: Str
	:param keep_fields: Fields that will be used.
	:type keep_fields: Iterable[str]
	:param stats: The various statistical measurements to be computed.
	:type stats: Iterable[str]
	:param report_threshold: The number of iterations before it prints out the feature number it's on. Default is 1000. Set to None to disable.
	:type report_threshold: Int
	:param write_batch_size: The number of zones that should be stored up before writing to disk.
	:type write_batch_size: Int
	:param use_points: Switch rasterstats to extract using gen_point_query instead of gen_zonal_stats. See rasterstats
		package documentation for complete information. Get_point_query will get the values of a raster at all vertex
		locations when provided with a polygon or line. If provided points, it will extract those point values. We set
		interpolation to the nearest to perform an exact extraction of the cell values. In this codebase's usage, it's
		assumed that the "features" parameter to this function will be a points dataset (still in the same CRS as the raster)
		when use_points is True. Additionally, when this is True, the `stats` argument to this function is ignored
		as only a single value will be extracted as the attribute `value` in the output CSV. Default is False.
	:type use_points: Bool
	:param inject_constants: A dictionary of field: value mappings to inject into every row. Useful if you plan to merge
		the data later. For example, a raster may be a single variable and date, and we're extracting many rasters. So
		for each zonal call, you could do something like inject_constants = {date: '2021-01-01', variable: 'et'}, which
		would produce headers in the CSV for "date" and "variable" and added values in the CSV of "2021-01-01", "et".
	:param kwargs: Passed through to rasterstats
	:return:
	:rtype: Union[str, Path, None]

	"""
	# Note the use of gen_zonal_stats, which uses a generator. That should mean that until we coerce it to a list on the
	# next line, each item isn't evaluated, which should prevent us from needing to store a geojson representation of
	# all the polygons at one time since we'll strip it off (it'd be bad to try to keep all of it.

	output_filepath: Optional[str] = None

	if not (
			isinstance(features, fiona.Collection) or (
				hasattr(features, "__iter__") and not
				(
					isinstance(features, str) or isinstance(features, bytes)
				)
			)
	):
		# If features isn't already a fiona collection instance or something else, we can iterate over.
		# A silly hack to get fiona to open GDB data by splitting it only if the input is a gdb data item, then providing
		# anything else as kwargs. But fiona requires the main item to be an arg, not a kwarg.
		if isinstance(features, str) or isinstance(features, Path):
			feats_open = safe_fiona_open(features)
			_feats_opened_in_function = True
	else:
		feats_open = features  # If it's a fiona instance, just use the open instance.
		_feats_opened_in_function = False  # But mark that we didn't open it, so we don't close it later.
	try:
		if not use_points:  # If we want to do zonal, open a zonal stats generator.
			zstats_results_geo = rasterstats.gen_zonal_stats(feats_open,
																raster,
																stats=stats,
																geojson_out=True,
																nodata=nodata_value,
																**kwargs
															)
			fieldnames = (*stats, *keep_fields)
			file_suffix = f"zonal_stats_nodata{nodata_value}"

		else:  # Otherwise, open a point query generator.
			# TODO: Need to make it convert the polygons to points here, otherwise it'll get the vertex data
			zstats_results_geo = rasterstats.gen_point_query(feats_open,
																raster,
																geojson_out=True,  # Need this to get extra attributes back.
																nodata=nodata_value,
																interpolate="nearest",  # Need this or else rasterstats uses a mix of nearby cells, even for single points.
																**kwargs)
			fieldnames = ("value", *keep_fields)  # When doing point queries, we get a field called "value" back with the raster value.
			file_suffix = f"point_query_nodata{nodata_value}"

		fieldnames_headers = (*fieldnames, *inject_constants.keys())  # This is separate because we use fieldnames later to pull out data - the constants are handled separately, but we need to write this to the CSV as a header.

		# Here's a first approach that still stores a lot in memory - it's commented out because we're instead
		# going to just generate them one by one and write them to a file directly.
		#
		# This next line is doing a lot of work. It's a dictionary comprehension inside a list comprehension -
		# we're going through each item in the results, then accessing just the properties key and constructing a new
		# dictionary just for the keys we want to keep - the keep fields (the key and a class field by default) and
		# the stats fields.
		# zstats_results = [{key: poly['properties'][key] for key in fieldnames} for poly in zstats_results_geo]

		i = 0
		output_filepath = os.path.join(str(output_folder), f"{filename}_{file_suffix}.csv")
		with open(output_filepath, 'w', newline='') as csv_file:
			writer = csv.DictWriter(csv_file, fieldnames=fieldnames_headers)
			writer.writeheader()
			results = []
			for poly in zstats_results_geo:  # Get the result for the polygon, then filter the keys with the dictionary comprehension below.
				result = {key: poly['properties'][key] for key in fieldnames}

				for key in result:  # Truncate the floats.
					if type(result[key]) is float:
						result[key] = f"{result[key]:.5f}"

				result = {**result, **inject_constants}  # Merge in the constants.

				i += 1
				results.append(result)
				if i % write_batch_size == 0:
					writer.writerows(results)  # Then write the lone result out one at a time to not store it all in RAM.
					results = []

				if report_threshold and i % report_threshold == 0:
					print(i)

			if results:  # Clear out any remaining items at the end.
				writer.writerows(results)
				print(i)
	finally:
		if _feats_opened_in_function:  # If we opened the fiona object here, close it. Otherwise, leave it open.
			feats_open.close()

	return output_filepath
