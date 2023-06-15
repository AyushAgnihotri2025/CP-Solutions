/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxLevelSum(root *TreeNode) int {
	if root == nil {
		return 0
	}
	level := 0
	sum := math.MinInt
	queue := make([]*TreeNode, 0)
	queue = append(queue, root)
	currentLevel := 0
	for len(queue) > 0 {
		currentLevelSize := len(queue)
		currentLevelSum := 0
		currentLevel++
		for i := 0; i < currentLevelSize; i++ {
			node := queue[i]
			currentLevelSum += node.Val
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		queue = queue[currentLevelSize:]
		if sum < currentLevelSum {
			sum = currentLevelSum
			level = currentLevel
		}
	}
	return level
}