import random

def generate_fake_input():
    return [random.random() for _ in range(41)]  # 41 features for NSL-KDD

if __name__ == '__main__':
    input_sample = generate_fake_input()
    print("Simulated Input:", input_sample)
    from predict import predict
    print("Prediction:", predict(input_sample))
