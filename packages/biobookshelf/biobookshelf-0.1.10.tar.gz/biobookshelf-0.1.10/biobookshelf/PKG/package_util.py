from biobookshelf.main import *

def Download_Data( dir_file, dir_remote, name_package ) :
    """
    Download large datafile of a PyPI package from a remote directory. If the file already exists, skip downloading and exit the funciton.
    download given file (relative directory within a package) from the remote directory (usually a Github directory, with sufficient number of data packs for Git-LFS pulls) to a current package
    """
    dir_file_download_flag = pkg_resources.resource_filename( name_package, f'{dir_file}.download_completed.flag' )
    if not os.path.exists( dir_file_download_flag ) :
        OS_Download( f'{dir_remote}{dir_file}', pkg_resources.resource_filename( name_package, dir_file ) )
        with open( dir_file_download_flag, 'w' ) as file :
            file.write( 'download completed at ' + TIME_GET_timestamp( ) )
        print( f"data file {dir_file} of the package {name_package} has been downloaded." )