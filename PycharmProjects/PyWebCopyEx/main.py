from pywebcopy import save_webpage

kwargs = {'zip_project_folder': False, 'load_images': False, 'over_write': True}

save_webpage(
   url='https://180atlas.com/index.html',
   project_folder='/Users/Franno/Documents/PythonWebCopyClones',
   **kwargs
)

print("All Done Cloning")