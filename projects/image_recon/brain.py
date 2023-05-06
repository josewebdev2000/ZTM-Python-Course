from imageai.Classification import ImageClassification
import os

def main() -> None:
    
    execution_path = os.getcwd()
    
    print("Giraffe Image Results: \n\n")
    detect_object(execution_path, 'resnet50-19c8e357.pth', os.path.join('pics', 'giraffe.jpg'))
    
    print("\n\nGodzilla Image Results: \n\n")
    detect_object(execution_path, 'resnet50-19c8e357.pth', os.path.join('pics', 'godzilla.jpg'))
    
    print("\n\nHouse Image Results: \n\n")
    
    detect_object(execution_path, 'resnet50-19c8e357.pth', os.path.join('pics', 'house.jpg'))

def detect_object(execution_path, model_path, image_path):
    
    prediction = ImageClassification()
    prediction.setModelTypeAsResNet50()
    prediction.setModelPath(os.path.join(execution_path, model_path))
    prediction.loadModel()
    
    predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, image_path), result_count = 5)
    
    for each_prediction, each_probability in zip(predictions, probabilities):
        print(each_prediction, ": ", each_probability)
    

if __name__ == "__main__":
    main()