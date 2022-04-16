class A:
    def feature_1(self):
        print("Feature 1 Working")

    def feature_2(self):
        print("Feature 2 Working")


class B(A):
    def feature_3(self):
        print("Feature 3 Working")

    def feature_4(self):
        print("Feature 4 Working")

b1 = B()
print("Single Level Inheritance")
b1.feature_1()
b1.feature_2()
b1.feature_3()
b1.feature_4()