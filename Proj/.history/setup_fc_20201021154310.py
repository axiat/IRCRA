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
    ],

    #脚本文件
    scripts=[
        "run_fc_train.sh"
        "run_fc_test.sh"
        "run_fc_sdk.sh"
    ],

    #数据文件
    package_data={
        "faceclassify.models":["facec.pt"],
    },

)


# python setup_app.py --help
# python setup_app.py --help-commands
# python setup_app.py build
# python setup_app.py install