import pymysql
import re


def start():
    while True:
        args = input('App>').split(' ')  # 命令行参数
        args_len = len(args)  # 命令行参数长度
        if args_len > 0 and args[0] != 'App':  # 命令开头必须是App开头
            print('请以App作为命令行的开头')
        else:
            if args[1] == '--help' or args[1] == '-h':  # 帮助
                help()
            elif args[1] == '--version' or args[1] == '-v':  # 版本
                version()
            elif args[1] == '--list' or args[1] == '-l':  # 列表
                if args_len == 2:  # 默认降序
                    list(True)
                elif args_len == 3 and (args[2] == 'ascend' or args[2] == 'asc'):  # 升序
                    list(False)
                else:
                    print('输入错误，请重试')
            elif re.match(r'--delete=\d+', args[1]) or re.match(r'-d=\d+', args[1]):  # 删除
                delete(args[1])
            elif args[1] == '--add' or args[1] == '-a':  # 增加
                if args_len == 12 and args[2] == '-n' and args[4] == '-i' and args[6] == '-e' and args[8] == '-m' and \
                        args[10] == '-h':  # 参数正确
                    add(args[3], args[5], args[7], args[9], args[11])
                else:
                    print('输入错误，请检查是否缺项/多项/顺序有误')
            elif re.match(r'--update=\d+', args[1]) or re.match(r'-u=\d+', args[1]):  # 修改
                update(args)
            elif args[1] == '--reset' or args[1] == '-r':  # 重置id
                reset()
            else:
                print('输入错误，请重试')


# 帮助信息-h --help
def help():
    print('''用例: App>App [选项]
    可用的选项:
      -h, --help                  显示帮助信息
      -v, --version               显示版本信息
      -a, --add                   增加信息
      -d, --delete                删除信息
      -u, --update                修改信息
      -l, --list                  显示信息
      -r, --reset                 更新id为从1开始连续自增
    注意: 命令行必须以App作为开头''')  # 帮助信息


# 版本信息-v --version
def version():
    print('App 1.0.0，为管理员对后台数据进行管理而设计，仅供内部使用，开发人员jyj')  # 版本号


# 显示信息-l --list
def list(flag):
    db = pymysql.connect(host='localhost', user='root', password='152935', db='dace', charset="utf8")
    cursor = db.cursor()
    if flag:  # 如果是默认显示，则降序排序
        cursor.execute("select * from dace01_student order by id desc")  # 降序
    else:
        cursor.execute("select * from dace01_student order by id asc")  # 升序
    result = cursor.fetchall()  # 获取所有数据
    print('当前数据库中一共有%s条数据' % len(result))
    for row in result:  # 遍历数据并输出
        print('id: %s, name: %s, number: %s, email: %s, phone: %s, hobby: %s' % (row[0], row[1], row[2], row[3], row[4],
                                                                                 row[5]))


# 删除信息-d --delete
def delete(content):
    content_id = content.split('=')[1]  # 获取id
    db = pymysql.connect(host='localhost', user='root', password='152935', db='dace', charset="utf8")
    try:
        with db.cursor() as cursor:
            sql = "DELETE FROM dace01_student WHERE `id` = %s"
            cursor.execute(sql, (content_id,))  # 执行删除
            db.commit()
            if cursor.rowcount > 0:  # 判断是否删除成功
                print("已成功删除id为{}的数据".format(content_id))
            else:
                print("未查询到此id")
    except Exception as e:
        db.rollback()  # 回滚
        print("发生错误: ", e)
    finally:
        db.close()  # 关闭连接


# 增加信息-a --add
def add(name, num, email, mobile, hobbit):
    db = pymysql.connect(host='localhost', user='root', password='152935', db='dace', charset="utf8")
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT MAX(id) FROM dace01_student")
            result = cursor.fetchone()  # 获取最大id
            max_id = result[0]
            if max_id is None:
                new_id = 1  # id为1
            else:
                new_id = max_id + 1  # id自增
            sql = """
            INSERT INTO dace01_student (id, name, num, email, mobile, hobbit)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (new_id, name, num, email, mobile, hobbit))  # 执行添加
            db.commit()
            if cursor.rowcount > 0:  # 判断是否添加成功
                print("已成功添加数据")
            else:
                print("添加数据失败")
    except Exception as e:
        db.rollback()  # 回滚
        print("发生错误: ", e)
    finally:
        db.close()  # 关闭连接


# 修改信息-u --update
def update(args):
    content_id = args[1].split('=')[1]  # 获取id
    content = args[2:]  # 获取修改指令和内容
    for element in content:
        if element == "-n":  # 如果修改的是name
            name = content[content.index("-n") + 1]  # 获取name内容
            db = pymysql.connect(host='localhost', user='root', password='152935', db='dace', charset="utf8")
            try:
                with db.cursor() as cursor:
                    sql = "update dace01_student set name = %s where id= %s "
                    cursor.execute(sql, (name, content_id,))  # 执行修改
                    db.commit()
                    if cursor.rowcount > 0:
                        print("已成功更新id为{}的数据name字段".format(content_id))
                    else:
                        print("未查询到此id")
            except Exception as e:
                db.rollback()  # 回滚
                print("发生错误: ", e)
            finally:
                db.close()
        elif element == "-i":  # 如果修改的是num
            num = content[content.index("-i") + 1]  # 获取num内容
            db = pymysql.connect(host='localhost', user='root', password='152935', db='dace', charset="utf8")
            try:
                with db.cursor() as cursor:
                    sql = "update dace01_student set num = %s where id= %s "
                    cursor.execute(sql, (num, content_id,))  # 执行修改
                    db.commit()
                    if cursor.rowcount > 0:  # 判断是否修改成功
                        print("已成功更新id为{}的数据学号字段".format(content_id))
                    else:
                        print("未查询到此id")
            except Exception as e:
                db.rollback()  # 回滚
                print("发生错误: ", e)
            finally:
                db.close()
        elif element == "-e":  # 如果修改的是email
            email = content[content.index("-e") + 1]  # 获取email内容
            db = pymysql.connect(host='localhost', user='root', password='152935', db='dace', charset="utf8")
            try:
                with db.cursor() as cursor:
                    sql = "update dace01_student set email = %s where id= %s"
                    cursor.execute(sql, (email, content_id,))  # 执行修改
                    db.commit()
                    if cursor.rowcount > 0:
                        print("已成功更新id为{}的数据email字段".format(content_id))
                    else:
                        print("未查询到此id")
            except Exception as e:
                db.rollback()  # 回滚
                print("发生错误: ", e)
            finally:
                db.close()  # 关闭连接
        elif element == "-m":  # 如果修改的是mobile
            mobile = content[content.index("-m") + 1]  # 获取mobile内容
            db = pymysql.connect(host='localhost', user='root', password='152935', db='dace', charset="utf8")
            try:
                with db.cursor() as cursor:
                    sql = "update dace01_student set mobile = %s where id= %s"
                    cursor.execute(sql, (mobile, content_id,))
                    db.commit()
                    if cursor.rowcount > 0:
                        print("已成功更新id为{}的数据电话字段".format(content_id))
                    else:
                        print("未查询到此id")
            except Exception as e:
                db.rollback()  # 回滚
                print("发生错误: ", e)
            finally:
                db.close()
        elif element == "-h":  # 如果修改的是hobbit
            hobbit = content[content.index("-h") + 1]
            db = pymysql.connect(host='localhost', user='root', password='152935', db='dace', charset="utf8")
            try:
                with db.cursor() as cursor:
                    sql = "update dace01_student set hobbit = %s where id= %s"
                    cursor.execute(sql, (hobbit, content_id,))
                    db.commit()
                    if cursor.rowcount > 0:
                        print("已成功更新id为{}的数据兴趣爱好字段".format(content_id))
                    else:
                        print("未查询到此id")
            except Exception as e:
                db.rollback()
                print("发生错误: ", e)
            finally:
                db.close()


# 重置id -r --reset
def reset():
    db = pymysql.connect(host='localhost', user='root', password='152935', db='dace', charset="utf8")
    try:
        with db.cursor() as cursor:
            # 分开执行每个ALTER TABLE语句
            sql1 = 'ALTER TABLE dace01_student DROP id'
            cursor.execute(sql1)  # 执行删除id
            db.commit()

            sql2 = 'ALTER TABLE dace01_student ADD id int(10) not null'
            cursor.execute(sql2)  # 执行添加id
            db.commit()

            sql3 = 'ALTER TABLE dace01_student MODIFY column id int(10) not null auto_increment, ADD PRIMARY KEY (id)'
            cursor.execute(sql3)  # 执行重置id
            db.commit()

            if cursor.rowcount > 0:  # 判断是否修改成功
                print("已成功更新id排列")
            else:
                print("未查询到此id")
    except Exception as e:
        db.rollback()  # 回滚
        print("发生错误: ", e)
    finally:
        db.close()


if __name__ == '__main__':
    start()  # 调用start函数
