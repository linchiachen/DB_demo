#!/usr/bin/env python3
# coding=utf-8
# -*- coding: UTF-8 -*-

from flask import Flask, request
import MySQLdb

app = Flask(__name__)



@app.route('/')
def index():
    form = """
    
    <form method="post" action="/action" >
        顯示可選課程
        <input type="submit" value="查詢">
        
    </form>
    
    <form method="post" action="/born" >
        請輸入學生ID(DXXX)、名字、性別(男/女)、系所(資工系/外語系)生成學生：<input name="s_id">
        <input name="s_name">
        <input name="s_g">
        <input name="s_d">
        
        <input type="submit" value="確認生成">

    </form>
    
    <form method="post" action="/die" >
        請輸入要刪除的學生ID：<input name="s_id">
        
        
        <input type="submit" value="確認刪除">

    </form>
    
  
    <form method="post" action="/student" >
        請輸入學生id查詢基本資料：<input name="s_id">

        <input type="submit" value="確認">

    </form>
    
    <form method="post" action="/curr" >
        請輸入學生id查詢課表和學分：<input name="s_id">

        <input type="submit" value="確認">

    </form>
    
    <form method="post" action="/add" >
        請輸入學生id、加選課號：<input name="s_id">
        <input name="c_id">

        <input type="submit" value="確定加選">

    </form>
    
    <form method="post" action="/delete" >
        請輸入學生id、退選課號：<input name="s_id">
        <input name="c_id">

        <input type="submit" value="確定退選">

    </form>
    
    """
    return form

#顯示可選課程
@app.route('/action', methods=['POST'])
def action1():

    # 建立資料庫連線
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="hj",
                           passwd="test1234",
                           db="testdb")

    query = "SELECT  cou_id,cou_name,cou_dept,cou_credit,cou_necessary,cou_maximum_people,cou_time1,cou_time2,t_name FROM course LEFT JOIN teacher on course.t_id=teacher.t_id ;"

    
    # 執行查詢 
    cursor = conn.cursor()
    cursor.execute(query)

    results = """
    <p><a href="/">返回</a></p>
    """
    # 取得並列出所有查詢結果
    for (description ) in cursor.fetchall():
        results += f"<p>{description}</p>"
    return f"分別對應:課號、課名、系所、學分數、是否為該系必修、人數上限、時間代號*2、授課老師 {results}"


#查學生基本資訊
@app.route('/student', methods=['POST'])
def action2():

    s_id = request.form.get("s_id")
    # 建立資料庫連線
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="hj",
                           passwd="test1234",
                           db="testdb")
    
    cursor = conn.cursor()
    
    results = """
    <p><a href="/">返回</a></p>
    """
    
    #先搜尋是否存在此學生 
    cursor.execute(" select  stu_id FROM student WHERE stu_id='{}' " .format(s_id))
    stu_id = cursor.fetchone()
    
    if stu_id is None:
         return f"無法查詢，此學生不存在 {results}"
         
    query = "SELECT * FROM student where stu_id LIKE '%{}%';".format(
        s_id)
   
    # 執行查詢 
    
    
    
    cursor.execute(query)

    
         
    # 取得並列出所有查詢結果
    for (description ) in cursor.fetchall():
        results += f"<p>{description}</p>"
    return results
    
#查學生的課表和當前總學分
@app.route('/curr', methods=['POST'])
def action3():

    s_id = request.form.get("s_id")
    # 建立資料庫連線
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="hj",
                           passwd="test1234",                     
                           db="testdb")

    cursor = conn.cursor()
    
    results = """
    <p><a href="/">返回</a></p>
    """
    
    #先搜尋是否存在此學生 
    cursor.execute(" select  stu_id FROM student WHERE stu_id='{}' " .format(s_id))
    stu_id = cursor.fetchone()
    
    if stu_id is None:
         return f"無法查詢，此學生不存在 {results}"
    
    
    #得到某個學生目前總學分
    cursor.execute( "select sum(cou_credit) from ( select curriculum.stu_id ,course.cou_id, course.cou_name, course.cou_credit from curriculum left join course on course.cou_id=curriculum.cou_id where stu_id='{}' GROUP BY course.cou_id ) as credit_count".format(s_id) )
    point = cursor.fetchone() 
   
   
    #得到他的課表和總學分
    #query ="SELECT curriculum.stu_id, curriculum.cou_id, course.cou_name, course.cou_credit, course.cou_dept ,course.cou_necessary from curriculum left join course on curriculum.cou_id= course.cou_id where stu_id='{}' order by cou_id;".format(s_id)
    query="SELECT curriculum.stu_id,curriculum.cou_id,abc.cou_name,abc.cou_dept,abc.cou_credit,abc.cou_necessary,abc.cou_maximum_people, abc.cou_time1 , abc.cou_time2,abc.t_name   FROM curriculum LEFT JOIN (SELECT  cou_id,cou_name,cou_dept,cou_credit,cou_necessary,cou_maximum_people,cou_time1,cou_time2,t_name FROM course LEFT JOIN teacher on course.t_id=teacher.t_id )  as abc on curriculum.cou_id = abc.cou_id where stu_id='{}' ORDER by curriculum.cou_id ;".format(s_id)

    # 執行查詢 
    
    cursor.execute(query)
  


    for (description ) in cursor.fetchall():
        results += f"<p>{description}</p>"
    return f'學號、課號、課名、所屬系所、學分、是否為該系所必修、教室容量、時間代號*2、授課老師   目前擁有{point[0]}學分 {results} '


#加選
@app.route('/add', methods=['POST'])
def actions4():
 
    s_id = request.form.get("s_id")
    c_id = request.form.get("c_id")
    # 建立資料庫連線
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="hj",
                           passwd="test1234",
                           db="testdb")
    # 欲查詢的 query 指令
    
    results = """
    <p><a href="/">返回</a></p>
    """
    cursor = conn.cursor()
    #先搜尋是否存在此學生 
    cursor.execute(" select  stu_id FROM student WHERE stu_id='{}' " .format(s_id))
    stu_id = cursor.fetchone()
    
    if stu_id is None:
         return f"無法加選，此學生不存在 {results}"
    
    
    if  c_id=='' : 
        return f'加選失敗，請輸入加選課號 \n{results}'
      
    if int(c_id)>38 or int(c_id)<1  :
        return f'課號只有1~37 \n{results}'
        
    
    
    #搜尋此學生是否已擁有這堂課
    cursor.execute(   "SELECT cou_id FROM curriculum where stu_id ='{0}'and cou_id ='{1}' ; ".format(s_id, c_id)    )
    now_cid = cursor.fetchone()
    
    if now_cid is None:
        pass
    else:    
        return  f'你已擁有這堂課{results}'
    
    #取得目前人數 
    cursor.execute(   "SELECT count(*) FROM curriculum WHERE cou_id='{1}' ".format(s_id, c_id)    )
    now_people = cursor.fetchone()
    
    #取得課堂人數限制
    cursor.execute("SELECT cou_maximum_people FROM course WHERE cou_id={1}".format(s_id, c_id)  )
    max_people = cursor.fetchone() 
    
    #print(now_people[0])  
    #print(max_people[0])  
    
    if( now_people[0]+1 >max_people[0] ) :
        return f'人數已滿不能加選 {results}'
    
  
    
        
        
    cursor.execute("select cou_time1 from course where cou_id='{1}';" .format(s_id, c_id)  )
    time1 = cursor.fetchone()
    cursor.execute("select cou_time2 from course where cou_id='{1}';" .format(s_id, c_id)  )
    time2 = cursor.fetchone()
    
    #取得課表時間 : 顯示除了當下輸入課程以外的時間 ，沒有考慮到重複輸入
    cursor.execute("select course.cou_time1,course.cou_time2 from curriculum left join course on curriculum.cou_id = course.cou_id   where stu_id='{0}' and course.cou_id <> '{1}';" .format(s_id, c_id)  )
    my_time = cursor.fetchall()
    
    #print(time1[0])
    #print(time2[0])
    #print(my_time)
    
    long = len(my_time)
    
    
    for i in range(0, long):
        for j in range(0,2):
            if( time1[0] == my_time[i][j] or time2[0] == my_time[i][j] ):
                return f'課堂時間衝突 \n{results}'
            
            
    # 確認課程是否為該學生的本科系必修課程，並進行擋修的動作
    cursor.execute("SELECT cou_id FROM course WHERE cou_id='{0}' AND cou_dept=(SELECT stu_dept FROM student WHERE stu_id='{1}') AND cou_necessary='是'".format(c_id, s_id))
    required_course = cursor.fetchone()

    if required_course is None:
        return f'加選失敗，您只能加選本科系的必修課程\n{results}'
    

    # 檢查學生是否已經選擇了同名的課程
    cursor.execute("SELECT COUNT(*) FROM curriculum AS c INNER JOIN course AS co ON c.cou_id = co.cou_id WHERE c.stu_id='{0}' AND co.cou_name=(SELECT cou_name FROM course WHERE cou_id='{1}')".format(s_id, c_id))
    duplicate_course_count = cursor.fetchone()[0]

    if duplicate_course_count > 0:
        return f'加選失敗，您已經選擇了同名的課程\n{results}'


    #得到某個學生目前總學分
    cursor.execute( "select sum(cou_credit) from ( select curriculum.stu_id ,course.cou_id, course.cou_name, course.cou_credit from curriculum left join course on course.cou_id=curriculum.cou_id where stu_id='{0}' GROUP BY course.cou_id ) as credit_count".format(s_id,c_id) )
    point = cursor.fetchone() 
    #print(point[0])
    
    #拿到這堂課學分
    cursor.execute(  "SELECT cou_credit FROM course WHERE cou_id='{1}' ; ".format(s_id, c_id)    )
    credit = cursor.fetchone()
    #print(credit[0])
   
   
    if point[0] + credit[0] >30 :
        return f'加選失敗\n您已超過30學分\n 您加選的課是{credit[0]}學分\n 您已經擁有 {point[0]} 學分 {results}'  

    
    
    query = "INSERT INTO curriculum(stu_id,cou_id) values ('{0}', '{1}')".format(s_id, c_id)  
    cursor.execute(query)  
    conn.commit()
        
    
    return f'加選成功\n 目前人數: {now_people[0]+1}/{max_people[0]} {results}'
    
#退選 
@app.route('/delete', methods=['POST'])
def actions5():

    s_id = request.form.get("s_id")
    c_id = request.form.get("c_id")
    # 建立資料庫連線
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="hj",
                           passwd="test1234",
                           db="testdb")

    cursor = conn.cursor()
    
    results = """
    <p><a href="/">返回</a></p>
    """
    
    cursor = conn.cursor()
    #先搜尋是否存在此學生 
    cursor.execute(" select  stu_id FROM student WHERE stu_id='{}' " .format(s_id))
    stu_id = cursor.fetchone()
    
    if stu_id is None:
         return f"無法退選，此學生不存在 {results}"
    
    if  c_id=='' : 
        return f"退選失敗，請輸入學生id、退選課號 \n{results}"
    
   
    
    cursor.execute(   "SELECT cou_id FROM curriculum where stu_id ='{0}'and cou_id ='{1}' ; ".format(s_id, c_id)    )
    del_id = cursor.fetchone()
    
    if del_id is None : 
        return f"退選失敗，你並沒有選這門課 \n {results}"
    
    
    #得到某個學生目前總學分
    cursor.execute( "select sum(cou_credit) from ( select curriculum.stu_id ,course.cou_id, course.cou_name, course.cou_credit from curriculum left join course on course.cou_id=curriculum.cou_id where stu_id='{0}' GROUP BY course.cou_id ) as credit_count".format(s_id,c_id) )
    point = cursor.fetchone() 
    #print(point[0])
    
    #拿到這堂課學分
    cursor.execute(   "SELECT cou_credit FROM course WHERE cou_id='{1}' ; ".format(s_id, c_id)    )
    credit = cursor.fetchone()
    #print(credit[0])
   
    point2=point[0]
    if point[0] - credit[0] <9 :
        return f'退選失敗\n您已小於9學分\n 您退選的課是{credit[0]}學分\n 您原本擁有 {point[0]} 學分 \n {results}'
        
        
    
    #確認退選的科目是不是必修
    cursor.execute( "SELECT cou_necessary FROM course WHERE cou_id='{1}' " .format(s_id, c_id)   )
    yn = cursor.fetchone()
    
    #print(yn[0])
    
        
    
    #確認科目是否與學生同系 
    #這門課的系
    cursor.execute( "SELECT cou_dept FROM course WHERE cou_id='{1}' " .format(s_id, c_id)   )
    c_d = cursor.fetchone()
  
    #print(yn2[0])
    
    #學生的系級
    cursor.execute( "SELECT stu_dept FROM student WHERE stu_id='{0}' " .format(s_id, c_id)   )
    s_d = cursor.fetchone()
  
    #print(yn3[0])
   
   
    # 執行查詢 
    query = "DELETE FROM curriculum where stu_id ='{0}' and  cou_id = {1}".format(
        s_id, c_id)
    cursor.execute(query)
    conn.commit()
    
    
    
    # 取得並列出所有查詢結果
    

        
    if  yn[0] == "是" and c_d[0] == s_d[0]:
        return f"警告:你退選了你所屬系的必修課程 \n {results}"
    else    :
        return f"退選成功 \n{results}"
    
 
@app.route('/born', methods=['POST'])
def action6():

    s_id = request.form.get("s_id")
    s_name = request.form.get("s_name")
    s_g = request.form.get("s_g")
    s_d = request.form.get("s_d")   
    
    #限制已經存在的學生
    # 
    if  len(s_id)!=4 or s_id[0]!='D' or s_id[1:4].isnumeric() != 1 or s_id=='' :
        #print(s_id)
        return "格式錯誤"
       
    if s_name =='':
        return "請輸入名字"
     
    check=1
    if s_g == '男' or s_g == '女':
        check = 0;
        
    if check or s_g=='':
        return "性別錯誤"
        
    check2=1
    
    if s_d == '資工系' or s_d == '外語系' :
        check2 = 0;
     
    if check2 or s_d=='':
        return "只有資工系和外語系"
    
    # 建立資料庫連線
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="hj",
                           passwd="test1234",
                           db="testdb")
    # 欲查詢的 query 指令
    cursor = conn.cursor()
  
    query  = " INSERT INTO student (stu_id, stu_name, stu_gender, stu_dept) VALUES ('{0}', '{1}', '{2}', '{3}') ".format(s_id, s_name, s_g, s_d) 
    cursor.execute(query)
    
    
    if s_d == "資工系" :
    
        query2 =  "INSERT INTO curriculum (stu_id,cou_id) VALUES ('{}' ,'1')" .format(s_id)
        cursor.execute(query2)
        
        
        query3 =  "INSERT INTO curriculum (stu_id,cou_id) VALUES ('{}' ,'2')" .format(s_id)
        cursor.execute(query3)
        
        
        query4 =  "INSERT INTO curriculum (stu_id,cou_id) VALUES ('{}' ,'3')" .format(s_id)
        cursor.execute(query4)
        
        
        query5 =  "INSERT INTO curriculum (stu_id,cou_id) VALUES ('{}' ,'4')" .format(s_id)
        cursor.execute(query5)
        
        
        query6 =  "INSERT INTO curriculum (stu_id,cou_id) VALUES ('{}' ,'5')" .format(s_id)
        cursor.execute(query6)
        
    if s_d == "外語系" :
    
        query2 =  "INSERT INTO curriculum (stu_id,cou_id) VALUES ('{}' ,'10')" .format(s_id)
        cursor.execute(query2)
        
        
        query3 =  "INSERT INTO curriculum (stu_id,cou_id) VALUES ('{}' ,'11')" .format(s_id)
        cursor.execute(query3)
        
        
        query4 =  "INSERT INTO curriculum (stu_id,cou_id) VALUES ('{}' ,'16')" .format(s_id)
        cursor.execute(query4)
        
        
        query5 =  "INSERT INTO curriculum (stu_id,cou_id) VALUES ('{}' ,'17')" .format(s_id)
        cursor.execute(query5)
        
        
        query6 =  "INSERT INTO curriculum (stu_id,cou_id) VALUES ('{}' ,'18')" .format(s_id)
        cursor.execute(query6) 
        
    conn.commit()
        
   
        
    results = """
    <p><a href="/">返回</a></p>
    """

    return  f"生成成功 \n {results}"

@app.route('/die', methods=['POST'])
def action7():

    s_id = request.form.get("s_id")
   
    
    # 建立資料庫連線
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="hj",
                           passwd="test1234",
                           db="testdb")
       
    cursor = conn.cursor()
    results = """
    <p><a href="/">返回</a></p>
    """
    #先搜尋是否存在此學生 
    cursor.execute(" select  stu_id FROM student WHERE stu_id='{}' " .format(s_id))
    stu_id = cursor.fetchone()
    
    if stu_id is None:
         return f"無法刪除，此學生不存在 {results}"
         
    cursor.execute(" DELETE FROM student WHERE stu_id='{}' " .format(s_id))
       
    cursor.execute(" DELETE FROM curriculum WHERE stu_id='{}' " .format(s_id))
    
    
    conn.commit()  
    
    
    return  f"刪除成功 \n {results}"