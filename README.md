### **Dokumentasi Backend TensorFlow.js: Menggunakan Model untuk Prediksi**

#### 1. **Memuat Model Menggunakan `tf.loadLayersModel`**

Sebelum menggunakan model untuk prediksi, Anda perlu memuat model terlebih dahulu. Fungsi `tf.loadLayersModel` digunakan untuk memuat model yang sudah dilatih dari file sistem lokal atau URL.

##### **Contoh Penggunaan**:
```javascript
const tf = require('@tensorflow/tfjs-node');

// Memuat model yang telah dilatih dari file sistem lokal
const modelPath = 'file://path/to/your/model/model.json';
const model = await tf.loadLayersModel(modelPath);
```

**Penjelasan**:
- **`tf.loadLayersModel`**: Fungsi ini memuat model yang disimpan dalam format JSON dan file weights terkait. Pastikan model `.json` dan file weights berada di direktori yang benar.

#### 2. **Preprocessing Gambar**

Setelah model dimuat, Anda perlu melakukan preprocessing pada gambar input agar dapat diberikan ke model untuk prediksi. Di bawah ini adalah contoh fungsi yang melakukan decoding gambar, resize, normalisasi, dan menambahkan dimensi batch untuk input.

##### **Fungsi Preprocessing Gambar**:

```javascript
const tf = require('@tensorflow/tfjs-node');

async function preprocessImage(imageBuffer, config) {
  let imageTensor;

  // Decode gambar menjadi tensor dengan 3 channel (RGB atau Grayscale)
  if (config.preprocess_image.color_mode === 'grayscale') {
    imageTensor = tf.node.decodeImage(imageBuffer, 1);  // Grayscale (1 channel)
  } else {
    imageTensor = tf.node.decodeImage(imageBuffer, 3);  // RGB (3 channels)
  }

  // Resize gambar ke ukuran yang sesuai (misal 120x120)
  imageTensor = imageTensor.resizeBilinear(config.preprocess_image.resize_shape);

  // Normalisasi gambar (piksel dari 0-255 menjadi 0-1)
  if (config.preprocess_image.normalize) {
    imageTensor = imageTensor.toFloat().div(config.preprocess_image.scaling_factor);
  }

  // Menambahkan dimensi batch
  return imageTensor.expandDims(0);  // Mengubah ukuran tensor menjadi [1, height, width, channels]
}
```

**Penjelasan**:
- **`tf.node.decodeImage(imageBuffer, channels)`**: Fungsi ini digunakan untuk mendecode gambar menjadi tensor. Anda dapat memilih jumlah channel gambar (1 untuk grayscale atau 3 untuk RGB).
- **`resizeBilinear(config.preprocess_image.resize_shape)`**: Resize gambar ke ukuran yang diinginkan, sesuai dengan input yang diharapkan oleh model (misalnya, 120x120).
- **`toFloat().div(scaling_factor)`**: Normalisasi gambar dengan mengubah tipe data gambar menjadi `float32` dan membaginya dengan faktor skala (biasanya 255 untuk mengubah piksel dari 0-255 menjadi 0-1).
- **`expandDims(0)`**: Menambahkan dimensi batch ke tensor, menjadikannya bentuk `[1, height, width, channels]` untuk disesuaikan dengan format input model.

##### **Contoh Penggunaan Preprocessing**:

```javascript
const config = {
  preprocess_image: {
    color_mode: 'rgb',        // Pilihan: 'grayscale' atau 'rgb'
    resize_shape: [120, 120],  // Ukuran gambar yang diinginkan
    normalize: true,          // Normalisasi (0-1)
    scaling_factor: 255.0     // Faktor normalisasi (untuk rentang 0-255)
  }
};

// Buffer gambar yang diterima, misalnya dari file upload atau request
const imageBuffer = fs.readFileSync('path/to/image.jpg');

// Preprocessing gambar
const imageTensor = await preprocessImage(imageBuffer, config);
```

#### 3. **Memprediksi Menggunakan Model**

Setelah gambar diproses menjadi tensor yang sesuai, Anda dapat memberikannya ke model untuk melakukan prediksi.

##### **Contoh Prediksi**:

```javascript
// Prediksi menggunakan model yang sudah dimuat
const predictions = await model.predict(imageTensor);

// Menampilkan hasil prediksi
console.log(predictions);
```

**Penjelasan**:
- **`model.predict(imageTensor)`**: Fungsi ini digunakan untuk mendapatkan prediksi dari model dengan memberikan input tensor (`imageTensor`). Model akan mengembalikan hasil berupa tensor yang berisi output prediksi.
- Output prediksi bisa berupa klasifikasi (untuk model klasifikasi) atau deteksi objek (untuk model seperti YOLO).


### **Ringkasan Dokumentasi**:

1. **Memuat Model**: Gunakan `tf.loadLayersModel` untuk memuat model dari file JSON.
2. **Preprocessing Gambar**: Gunakan `tf.node.decodeImage` untuk mendecode gambar, resize dengan `resizeBilinear`, normalisasi dengan `toFloat().div()`, dan tambahkan dimensi batch dengan `expandDims(0)`.
3. **Prediksi**: Gunakan `model.predict()` untuk mendapatkan prediksi dari model.
4. **Menerima Gambar di Express.js**: Gunakan Multer untuk menangani upload gambar dan mengirimkan hasil prediksi melalui endpoint Express.

Jika ada bagian yang perlu dijelaskan lebih lanjut atau contoh lainnya, beri tahu saya! 😊