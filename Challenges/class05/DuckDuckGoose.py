from queue import Queue

def DuckDuckGoose(*players, goose):
    """
    This function takes a list of players and the goose number and then
    moves the goose to the next player's position.
    """
    # Create a queue of players

    player_queue = Queue()

    for player in players:
        player_queue.enqueue(player)

    else:
        while player_queue.front != player_queue.last:
            # Move the goose to the next player's position
            for i in range(goose):
                if i == goose-1:
                    player_queue.dequeue()
                else:
                    player_queue.enqueue(player_queue.dequeue())

            # Return the player at the end of the queue
        return player_queue.front.value


if __name__ == '__main__':
    print(DuckDuckGoose('A', 'B', 'C', 'D', 'E', goose=3))
