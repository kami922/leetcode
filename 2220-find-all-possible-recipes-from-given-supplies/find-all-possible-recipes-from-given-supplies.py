from collections import deque, defaultdict

class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        graph = defaultdict(list)  # ingredient -> list of recipes
        indegree = {}  # recipe -> count of needed ingredients
        available = set(supplies)
        result = []

        # Step 1: Build graph and indegree map
        for i, recipe in enumerate(recipes):
            indegree[recipe] = len(ingredients[i])
            for ing in ingredients[i]:
                graph[ing].append(recipe)

        # Step 2: Perform BFS
        queue = deque(supplies)

        while queue:
            item = queue.popleft()
            if item not in graph:
                continue

            for recipe in graph[item]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    result.append(recipe)
                    queue.append(recipe)

        return result