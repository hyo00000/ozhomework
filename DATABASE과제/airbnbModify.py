import pymysql

# 데이터베이스 연결 설정
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='water1342',
    db='airbnb',
)

quantity_sold = 10  
product_id = 1  
new_email = 'new_email@example.com'  
customer_id = 1 
order_id = 1  

try:
    #1번 새로운 제품 추가
    with conn.cursor() as cursor:
        sql = "INSERT INTO Products (productName, price, stockQuantity) VALUES (%s, %s, %s)"
        cursor.execute(sql, ('Python Book', 29.99, 60))
        conn.commit()

    #2번 고객 목록 조회
        sql = "SELECT * FROM Customers"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print(row)

    #3번 제품 재고 업데이트
        sql_update_stock = "UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s"
        cursor.execute(sql_update_stock, (quantity_sold, product_id))

    #4번 고객별 총 주문 금액 계산
        sql = "SELECT customerID, SUM(totalAmount) FROM Orders GROUP BY customerID"
        cursor.execute(sql)
        for row in cursor.fetchall():
            print(row)

    #5번 고객 이메일 업데이트
        sql = "UPDATE Customers SET email = %s WHERE customerID = %s"
        cursor.execute(sql, (new_email, customer_id))
        conn.commit()

    #6번 주문 취소
        sql = "DELETE FROM Orders WHERE orderID = %s"
        cursor.execute(sql, (order_id,))
        conn.commit()

    #7번 특정 체품 검색
        sql = "SELECT * FROM Products WHERE productName LIKE %s"
        cursor.execute(sql, ('%Staff%'))
        for row in cursor.fetchall():
            print(row)

    #8번 특정 고객의 모든 주문 조회
        sql = "SELECT * FROM Orders WHERE customerID = %s"
        cursor.execute(sql, (1,))
        for row in cursor.fetchall():
            print(row)

    #9번 가장 많이 주문한 고객 찾기
        sql = "SELECT customerID, COUNT(*) as orderCount FROM Orders GROUP BY customerID ORDER BY orderCount DESC LIMIT 1"
        cursor.execute(sql)
        top_customer = cursor.fetchone()
        print(f"Top Customer ID: {top_customer[0]}, Orders: {top_customer[1]}")
        

finally:
    conn.close()

