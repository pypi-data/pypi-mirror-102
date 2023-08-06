import os



from tensorflow.python.keras.models import load_model

from graphmanagerlib.Data_for_gcn import get_data, load_train_test_split
from graphmanagerlib.Node import Node


from stellargraph import StellarGraph
from stellargraph.mapper import FullBatchNodeGenerator, pd



from sklearn import preprocessing, model_selection

from tensorflow.python.keras.callbacks import EarlyStopping
from Model_formation import CreateTrainAndSaveGCN


class GraphManager :
    def __init__(self, documents,save_dataset_fd):
        self.save_dataset_path = get_data(documents=documents,save_dataset_fd=save_dataset_fd)

    def CreateTrainAndSaveGCN(self):
        traindata, testdata = load_train_test_split(self.save_dataset_path)

        CreateTrainAndSaveGCN(traindata, testdata)

        print ("===== Modèle entrainé et sauvegardé =====")


def singlePrediction(modelPath,document):
    reconstructed_model = load_model(modelPath)

    documentNodes = document[0].nodes
    inputSize = reconstructed_model.input_shape[0][1]
    while len(documentNodes) < inputSize:
        documentNodes.append(Node(XMin=-1, YMin=-1, XMax=-1, YMax=-1, Tag='null'))

    nodes, edges, tags = DataTransformer().get_data(document, tags=pd.DataFrame(['undefined']))
    nodes.reset_index(inplace=True)
    nodesSubject = nodes['tag']

    nodes['tag'] = nodes['tag'].replace('undefined', 0)

    G = StellarGraph(nodes, edges)
    generator = FullBatchNodeGenerator(G, method="gcn")

    target_encoding = preprocessing.LabelBinarizer()
    targets = target_encoding.fit_transform(nodesSubject)
    all_gen = generator.flow(nodesSubject.index, targets)

    ##TRANSPOSE ?
    # check model generalisation on the test set
    (loss, accuracy) = reconstructed_model.evaluate(all_gen)
    print(f"Test set: loss = {loss}, accuracy = {accuracy}")

    all_predictions = reconstructed_model.predict(all_gen)

    node_predictions = target_encoding.inverse_transform(all_predictions.squeeze())

    df = pd.DataFrame({"Predicted": node_predictions, "True": nodesSubject})
    df.head(20)
    print(df.to_string())



