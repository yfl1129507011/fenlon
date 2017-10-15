# 基本配置类
class Cfg:
    SECRET_KEY = b'_@8a!+<fenlon>+0(-7%@_'  # 密钥


# 生产配置类
class ProductCfg(Cfg):
    DEBUG = False
    # mysql配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/fenlon?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


# 开发配置类
class DevelopmentCfg(Cfg):
    DEBUG = True
    # mysql配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/fenlon?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


config = {
    'development': DevelopmentCfg,
    'product': ProductCfg,
    'default': ProductCfg
}