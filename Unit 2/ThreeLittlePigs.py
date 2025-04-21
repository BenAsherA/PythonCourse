def build_house(amount: int):
    pig1bricks = int(amount / 100)
    pig2bricks = int(amount % 100 / 10)
    pig3bricks = int(amount%10)
    total_bricks = pig1bricks + pig2bricks + pig3bricks
    brick_average = total_bricks//3
    print (total_bricks)
    print (brick_average)
    print (total_bricks - brick_average * 3)
    print(total_bricks == brick_average * 3)
build_house(177)