
from onnx import onnx_pb
import onnx

def is_topsort(model):
    queue = [model]
    namespace = set()
    while queue:
        next_level = []
        for q in queue:
            # if q is model, push q.graph (GraphProto)
            if isinstance(q, onnx_pb.ModelProto):
                next_level.append(q.graph)
            # if q is model.graph, push q.node.attribute (AttributeProto)
            if isinstance(q, onnx_pb.GraphProto):
                for n in q.initializer:
                    namespace.add(n.name)
                for n in q.input:
                    namespace.add(n.name)
                for n in q.node:
                    for inp in n.input:
                        assert inp in namespace
                    for out in n.output:
                        namespace.add(out)
                    for attr in n.attribute:
                        next_level.append(attr)
                    
            # if q is model.graph.node.attribute, push q.g and q.graphs (GraphProto)
            if isinstance(q, onnx_pb.AttributeProto):
                next_level.append(q.g)
                for n in q.graphs:
                    next_level.append(n)
        queue = next_level
    return True

def repair_model(model):
    return []

#print(is_topsort(onnx.load(r"C:\Users\tomwi\Documents\tfhubmodels\bit-m-r50x1\model.onnx")))

print(is_topsort(onnx.load(r"C:\Users\tomwi\OneDrive - Microsoft\ONNX\onnxconverter-common\fp16problem\melgen_fs_opset11_new.onnx")))