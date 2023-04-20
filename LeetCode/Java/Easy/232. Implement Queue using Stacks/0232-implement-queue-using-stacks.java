class MyQueue {
    int arr[]=new int[1000];
    int front=0,rear=0;
    public MyQueue() {

    }
    public void push(int x) {
        if(isFull()) return;
        arr[rear]=x;
        rear++;
    }
    
    public int pop() {
        if(empty()) return 0;
        int x=arr[front];
        front++;
        return x;
    }
    
    public int peek() {
        int p=arr[front];
        return p;
    }
    
    public boolean empty() {
        if(front==rear) return true;
        return false;
    }
    public boolean isFull() {
        if(rear==arr.length) return true;
        return false;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */