from factual_scene_graph.evaluation.synonym_dictionary import SynonymDictionary

if __name__ == "__main__":
    synonym_dict = SynonymDictionary('src/factual_scene_graph/evaluation/resources/english.exceptions',
                                     'src/factual_scene_graph/evaluation/resources/english.synsets')
    print(synonym_dict.get_stem_synsets('write_down'))