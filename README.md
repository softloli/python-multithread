# python-multithread
python 多线程学习

Python提供了Condition对象。它除了具有acquire和release方法之外，还提供了wait和notify方法。线程首先acquire一个条件变量锁。如果条件不足，则该线程wait，如果满足就执行线程，甚至可以notify其他线程。其他处于wait状态的线程接到通知后会重新判断条件。

条件变量可以看成不同的线程先后acquire获得锁，如果不满足条件，可以理解为被扔到一个（Lock或RLock）的waiting池。直达其他线程notify之后再重新判断条件。


queue内部实现了相关的锁，如果queue的为空，则get元素的时候会被阻塞，知道队列里面被其他线程写入数据。同理，当写入数据的时候，如果元素个数大于队列的长度，也会被阻塞。也就是在 put 或 get的时候都会获得Lock。
