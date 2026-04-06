import random
class LLMClass:
    def __init__(self):
        print('LLM created...')
    def predict(self,prompt):
        
        response_list=[
            'AI stand for Artificial Intelligence',
            'ML stand for Machine Learning',
            'DL stand for Deep Learning',
            'NLP stand for Natural Language Processing',
            'CV stand for Computer Vision',
            'RL stand for Reinforcement Learning',
            'GAN stand for Generative Adversarial Network',
            'CNN stand for Convolutional Neural Network',
            'RNN stand for Recurrent Neural Network',
            'Transformer stand for Transformer'
        ]
        return {'response':random.choice(response_list)}
LLM=LLMClass()
print(LLM.predict('What is AI?'))