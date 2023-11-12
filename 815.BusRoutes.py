from typing import List
import collections

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # If the source is the same as the target, we don't need to take any buses.
        if source == target:
            return 0

        # Create a defaultdict to represent the graph where keys are bus stops and values are lists of buses that pass through that stop.
        graph = collections.defaultdict(list)
        
        # A set to keep track of buses that have been used to avoid duplicates.
        usedBuses = set()

        # Populate the graph based on the given routes.
        for i in range(len(routes)):
            for route in routes[i]:
                graph[route].append(i)

        # Initialize answer to track the number of buses taken.
        ans = 0

        # Use a deque for the breadth-first search starting from the source bus stop.
        q = collections.deque([source])

        # Perform breadth-first search
        while q:
            ans += 1
            for _ in range(len(q)):
                # Explore each bus stop in the current level of the search.
                current_stop = q.popleft()
                for bus in graph[current_stop]:
                    # Check if the bus has already been used.
                    if bus in usedBuses:
                        continue
                    usedBuses.add(bus)
                    for nextRoute in routes[bus]:
                        # Check if the destination is reached.
                        if nextRoute == target:
                            return ans
                        # Add the next bus stop to the queue for further exploration.
                        q.append(nextRoute)

        # If no path is found, return -1.
        return -1
