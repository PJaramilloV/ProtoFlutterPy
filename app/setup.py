# setup.py
import os
from init import safe_path_to
from setuptools import setup
from Cython.Build import cythonize
from models.dummy_nn import main as nn_main
from models.dummy_lr import main as lr_main

build_dir = safe_path_to('build')
compile_options = {
    'build_ext': {
        'build_lib': build_dir,  # Build output directory
        'build_temp': os.path.join(build_dir, 'tmp'),  # Temp build files
    }
}

# train models
nn_main()
lr_main()

# build Cython extension
setup(
    ext_modules=cythonize("inference_cython.pyx", compiler_directives={'language_level': "3"}),
    options = compile_options
)


###### Android App ######
# from distutils.core import Extension

# android_ndk = '/path/to/your/ndk'
# target_arch = 'arm64-v8a'

# # Specify the Cython extension
# ext_modules = [
#     Extension(
#         'inference_cython',        # The name of your extension
#         ['inference_cython.pyx'],  
#         libraries=[],
#         extra_compile_args=['-std=c++11', '-O3'],
#         extra_link_args=['-L{}'.format(os.path.join(android_ndk, 'platforms', 'android-21', 'arch-{}'.format(target_arch), 'usr', 'lib'))],
#         include_dirs=[android_ndk],  # NDK headers
#     )
# ]

# setup(
#     name='inference_cython',
#     ext_modules=cythonize(ext_modules),
#     options = compile_options
# )


###### iOS App ######
# from distutils.core import Extension

# ios_sdk_path = '/path/to/ios/sdk'
# target_arch = 'arm64'

# ext_modules = [
#     Extension(
#         'inference_cython',        # The name of your extension
#         ['inference_cython.pyx'],  
#         libraries=[],
#         extra_compile_args=['-arch', target_arch, '-O3'],
#         extra_link_args=['-L{}'.format(os.path.join(ios_sdk_path, 'usr', 'lib', 'arm64'))],
#         include_dirs=[os.path.join(ios_sdk_path, 'usr', 'include')],
#     )
# ]

# setup(
#     name='inference_cython',
#     ext_modules=cythonize(ext_modules),
#     options = compile_options
# )