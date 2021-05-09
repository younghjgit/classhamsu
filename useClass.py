class food:
    food_count = 0

    def __init__(self, name, price, taste, topping):
        self.name = name
        self.price = price
        self.taste = taste
        self.topping = topping
        food.food_count +=1

    def info(self):
            print(f'음식: {self.name}')
            print(f'가격: {self.price}')
            print(f'맛: {self.taste}')
            print(f'토핑: {self.topping}')
            print()

    def order(self, topping_num):
            print(self.topping[topping_num])



food1 = food("김치찌개", 7000, 8, ['돼지고기', '스팸','라면'])
food2 = food('햄버거', 6000, 9, ['치즈','감자튀김','콜라'])
food3 = food('짜장면',5000, 10, ['탕수육', '군만두', '유산슬'])

food1.info()
food2.info()
food3.info()

food1.order(2)
food2.order(1)
food3.order(0)

