# Testing

def auto_convert(model, feed_dict):
    pass

model0 = onnx.load(r"C:\Users\tomwi\OneDrive - Microsoft\ONNX\onnxconverter-common\fp16problem\convert_fp16\fs\fs.onnx")
model1 = convert_float_to_float16(model0, op_black_list=["CumSum"], node_black_list=skip_nodes)