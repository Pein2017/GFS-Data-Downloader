import xarray as xr
 
fn = '/home/HW/Pein/GFS/download_data/2023/20230101/gfs.0p25.2023010100.f000.grib2'
 
rh = xr.open_dataset(fn, engine='netcdf4', backend_kwargs={'filter_by_keys':{'typeOfLevel': 'isobaricInhPa', 'paramId':157}} )
pre = rh['isobaricInhPa'].data
 
gh = xr.open_dataset(fn, engine='cfgrib', backend_kwargs={'filter_by_keys':{'typeOfLevel': 'isobaricInhPa', 'paramId':156}})
 
gh['gh'].sel(isobaricInhPa=pre)
