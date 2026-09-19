class Pizza:
 def prepare(self):
    print("Order Pizza")
class Burger:
 def prepare(self):
    print("Order burger")
class Pasta:
 def prepare(self):
    print("Order pasta")

class OrderFactory:
  @staticmethod
  def order_food(food_type):
    if food_type == "pizza":
      return Pizza()
    elif food_type == "burger":
      return Burger()
    elif food_type == "pasta":
      return Pasta()
    else:
      raise ValueError("Invalid request")


order = OrderFactory.order_food("pizza")
order.prepare()
