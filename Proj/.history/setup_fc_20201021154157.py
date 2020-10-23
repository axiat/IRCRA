from distutils.core import setup

setup(
    name="face_classify",
    version="1.0",
    description="face_classify",
    author="Qinning Xu",
    # 包路径与python模块(.py扩展名文件)
    packages=[
        "faceclassify",
        "faceclassify.models",
        "faceclassify",
        "faceclassify",
        "faceclassify",
    ],

    #脚本文件
    scripts=[
        "run_fc.sh"
    ],

    #数据文件
    package_data={
        "faceclassify.models":["",""],
        "":["",""],
    },

)


# python setup_app.py --help
# python setup_app.py --help-commands
# python setup_app.py build
# python setup_app.py install