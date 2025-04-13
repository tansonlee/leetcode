class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = list(reversed(food))

        self.snake = deque([(0, 0)])
        self.snake_set = set([(0, 0)])

        self.dir_map = {
            "U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1),
        }

        self.score = 0

    def move(self, direction: str) -> int:
        dir = self.dir_map[direction]

        head_pos = self.snake[0]
        new_head_pos = (head_pos[0] + dir[0], head_pos[1] + dir[1])

        # In bounds
        if not (0 <= new_head_pos[0] < self.height and 0 <= new_head_pos[1] < self.width):
            return -1

    
        # Remove tail
        tail_pos = self.snake.pop()
        self.snake_set.remove(tail_pos)

        # Ate food
        if self.food:
            food_pos = tuple(self.food[-1])
            if new_head_pos == food_pos:
                self.score += 1
                self.food.pop()

                # Since it ate, put its tail back to grow
                self.snake_set.add(tail_pos)
                self.snake.append(tail_pos)
        
        # Hits own body
        if new_head_pos in self.snake_set:
            return -1

        # Add heaad
        self.snake_set.add(new_head_pos)
        self.snake.appendleft(new_head_pos)
        
        return self.score



        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
