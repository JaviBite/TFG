import matplotlib.pyplot as plt
import sys


def main():

    if len(sys.argv) > 1:
        logfile = sys.argv[1]
    else:
        print("Usage: " + sys.argv[0] + " <logfile>")
        exit()

    f = open(logfile, "r")

    loss_train = []
    loss_val = []
    for line in f:
        splitt = line.split(" ")
        loss_train.append(float(splitt[1]))
        loss_val.append(float(splitt[3]))
    
    axes = plt.gca()
    #axes.set_xlim([xmin,xmax])
    #axes.set_ylim([0,0.03])

    axes.set_ylabel('Loss')
    axes.set_xlabel('Epoch')
    axes.set_title('Loss evolution')

    plt.plot(loss_train, 'g', label="Train error")
    plt.plot(loss_val, 'b', label ="Validation error")

    handles, labels = axes.get_legend_handles_labels()

    # reverse the order
    axes.legend(handles[::-1], labels[::-1])

    plt.show()


if __name__ == '__main__':
    main()
    # eval.eval(model,test_loader)