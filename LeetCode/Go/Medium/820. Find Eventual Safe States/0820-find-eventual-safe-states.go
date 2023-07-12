func eventualSafeNodes(graph [][]int) []int {
    var res []int
    visited := make([]bool, len(graph))
    cache := make(map[int]bool)
    for i := 0; i < len(graph); i++ {
        if dfs(graph, visited, cache, i) {
            res = append(res, i)
        }
    }
    return res
}

func dfs(graph [][]int, visited []bool, cache map[int]bool, start int) bool {
    if status, ok := cache[start]; ok {
        return status
    }
    if visited[start] {
        visited[start] = false
        cache[start] = false
        return false
    }
    res := true
    visited[start] = true
    for _, neighbor := range graph[start] {
        if !dfs(graph, visited, cache, neighbor) {
            res = false
            break
        }
    }
    visited[start] = false
    cache[start] = res
    return res
}