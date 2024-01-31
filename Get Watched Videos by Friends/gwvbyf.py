


from ast import List
from collections import defaultdict, deque



class Solution:
    def watchedVideosByFriends(watchedVideos, friends, id, level):
        videos = defaultdict(int)
        q = deque([id])
        visited = set([id])

        while level > 0:
            for _ in range(len(q)):
                person = q.popleft()

                for friend in friends[person]:
                    if friend not in visited:
                        visited.add(friend)
                        q.append(friend)

                        if level == 1:
                            for vid in watchedVideos[friend]:
                                videos[vid] += 1
            
            level -= 1


    watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
    friends = [[1,2],[0,3],[0,3],[1,2]]
    id = 0
    level = 3
    person = 0

    watchedVideosByFriends(watchedVideos, friends, id, level)