from graphmanagerlib.Data_for_gcn import get_data, load_train_test_split
from graphmanagerlib.Model_formation import CreateTrainAndSaveGCN
from graphmanagerlib.Inference import predictionsUnique


class GraphManager:
    def __init__(self, documents, save_dataset_fd):
        self.save_dataset_path = get_data(documents=documents, save_dataset_fd=save_dataset_fd)

    def CreateTrainAndSaveGCN(self):
        traindata, testdata = load_train_test_split(self.save_dataset_path)
        CreateTrainAndSaveGCN(traindata, testdata, self.save_dataset_path)
        print("===== Modèle entrainé et sauvegardé =====")

    def single_prediction(self, saved_model_folder, prediction_dataset_folder, document_to_predict, labels_tab):
        return predictionsUnique(saved_model_folder, prediction_dataset_folder, document_to_predict, labels_tab)
