# 简介
1. database
2. caches
3. asynchronous task processing
4. authentication
5. role-base access 
6. REST API
7. internationlization 国际化
8. SQL/NoSQL
9. most common flask extensions
10. sending email to authentication using social media accounts 
11. write tests
12. Docker and jenkins 
13. deploy your application to cloud service 

# 第一章
[x] 配置 git repository
[x] 配置虚拟环境
[x] Docker 基础了解,创建 Dockerfile
[x] 配置第一个 Flask application

# 第二章
[x] 设计数据库表和关系
[ ] 增删改查
[ ] 学习如何定义数据库关系,约束，索引
[ ] 数据库版本控制

安装依赖
```
pip install flask-sqlalchemy 

# mysql
pymysql 

# postgres 
psycopg2 

# MSSQL
pyodbc

# Oracle
cx_Oracle
```

配置数据库 URI
```
# sqlite
    sqlite:///database.db
# MySQL
    mysql+pymysql://user:password@ip:port/db_name
# Postgres
    postgresql+psycopg2://user:password@ip:port/db_name
# MSSQL
    mssql+pyodbc://user:password@dsn_name
# Oracle
    oracle+cx_oracle://user:password@ip:port/db_name
```


