import matplotlib.pyplot as plt

# 定义一个绘制曲线的函数
def draw_curve(history):
    acc=history.history['acc']
    val_acc=history.history['val_acc']
    loss=history.history['loss']
    val_loss=history.history['val_loss']

    epochs = range(1,len(acc)+1)

    plt.plot(epochs,acc,'bo',label='Training acc')
    plt.plot(epochs,val_acc,'b',label='Validation acc')
    plt.title('Training and validation acc')
    plt.legend()
    plt.figure()

    plt.plot(epochs,loss,'bo',label='Training loss')
    plt.plot(epochs,val_loss,'b',label='Validation loss')
    plt.title('Training anda validation loss')
    plt.legend()

    plt.show()
    
# 定义一个绘制损失函数的函数
def draw_loss(history):
    loss=history.history['loss']
    val_loss=history.history['val_loss']

    epochs = range(1,len(loss)+1)

    plt.figure()

    plt.plot(epochs,loss,'bo',label='Training loss')
    plt.plot(epochs,val_loss,'b',label='Validation loss')
    plt.title('Training anda validation loss')
    plt.legend()

    plt.show()
    
# 定义一个绘制准确率的函数
def draw_acc(history):
    acc=history.history['acc']
    val_acc=history.history['val_acc']

    epochs = range(1,len(acc)+1)
    
    plt.figure()
    plt.plot(epochs,acc,'bo',label='Training acc')
    plt.plot(epochs,val_acc,'b',label='Validation acc')
    plt.title('Training and validation acc')
    plt.legend()

    plt.show()