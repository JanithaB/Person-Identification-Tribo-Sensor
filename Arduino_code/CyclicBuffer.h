class CyclicBuffer {
public:
  CyclicBuffer(int size) {
    this->size = size;
    buffer = new int[size];
    head = 0;
    tail = 0;
    valCount = 0;
  }

//Don't need this one. Didn't check correctness.
  ~CyclicBuffer() {
    delete[] buffer;
  }

  void push(int value) {
    buffer[head] = value;
    
    if (valCount>bufferSize()&&(head==tail)) {
      tail = (tail + 1) % size;
    }

    head = (head + 1) % size;
    valCount = valCount + 1;
  
  }

  int pop() {
    int value = buffer[tail];
    tail = (tail + 1) % size;
    return value;
  }

  bool isFull() {
    return ((head == tail) && valCount!=0);
  }

//Doesn't need this one. Didn't check correctness.
  bool isEmpty() {
    return head == (tail - 1) % size;
  }

  int bufferSize() {
    return size;
  }

  int buffmax() {
    int maxVal = 0;
  if (!isEmpty()) {
    
    for (int i = 0; i < bufferSize(); i++) {
      if (buffer[i] > maxVal) {
        maxVal = buffer[i];
      }
    }
    return maxVal;
  } else {
    // Handle the case of an empty buffer, e.g., return a default value or throw an error.
    return -1; // Placeholder value for an empty buffer
  }
}

  int getHead(){
    return head;
  }

//Doesn't need this one. Didn't check correctness.
  int peek() {
    if (!isEmpty()) {
      return buffer[tail];
    } else {
      // You may choose to handle this case differently, e.g., return a default value or throw an error.
      return -1; // Placeholder value for an empty buffer
    }
  }

  int get(int index) {
  if (index >= 0) {
    return buffer[(tail + index) % size];
  } else {
    // Handle negative index by adding it to the head position
    return buffer[(head + index) % size];
  }
}



  void clear() {
    head = tail;
  }

private:
  int size;
  int* buffer;
  int head;
  int tail;
  int valCount;
};
