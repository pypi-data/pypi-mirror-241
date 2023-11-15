from tketool.mlsample.NLSampleSource import NLSampleSourceBase
from tketool.mlsample.SampleSet import SampleSet
import json
from tketool.files import write_file_line


def convert_jsonl(datasource: NLSampleSourceBase, set_name: str, prompt_completion_fun,
                  target_path: str):
    row_lines = []
    for item in SampleSet(datasource, set_name):
        prompt, completion = prompt_completion_fun(item)
        row_data = {
            'prompt': prompt,
            'completion': completion
        }
        row_str = json.dumps(row_data)
        row_lines.append(row_str)

    write_file_line(target_path, row_lines)

