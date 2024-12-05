import 'dart:ffi';
import 'dart:io';

final library = DynamicLibrary.open(
    Platform.isAndroid ? '../app/build/inference_cython.so' :  
      /* Platform.isIOS ? */ '../app/build/inference_cython.dylib'
);

typedef PredictorC = Double Function(Double);
final predictorDart = library
    .lookup<NativeFunction<PredictorC>>('predict')
    .asFunction<double Function(double)>();

void main() {
  final output = predictorDart(5.0); // predict(5.0)
  print('Predicted Output: $output');
}
