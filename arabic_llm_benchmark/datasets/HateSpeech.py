from arabic_llm_benchmark.datasets.dataset_base import DatasetBase


class HateSpeechDataset(DatasetBase):
    def __init__(self, **kwargs):
        super(HateSpeechDataset, self).__init__(**kwargs)

    def citation(self):
        return """@inproceedings{mubarak2020overview,
          title={Overview of OSACT4 Arabic offensive language detection shared task},
          author={Mubarak, Hamdy and Darwish, Kareem and Magdy, Walid and Elsayed, Tamer and Al-Khalifa, Hend},
          booktitle={Proceedings of the 4th Workshop on open-source arabic corpora and processing tools, with a shared task on offensive language detection},
          pages={48--52},
          year={2020}
        }"""

    def get_data_sample(self):
        return {"input": "ايه اللي انت بتقوله ده يا اوروبي يا متخلف", "label": "HS"}

    def load_data(self, data_path, no_labels=False):
        # TODO: modify to iterator
        # Format: text \t hatespeech_label
        data = []
        with open(data_path, "r") as fp:
            for line_idx, line in enumerate(fp):
                text, label = line.split("\t")
                label = label.strip()
                data.append({"input": text, "label": label, "line_number": line_idx})

        return data