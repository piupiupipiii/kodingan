from PIL import Image, ImageFilter
import numpy as np
  
def apply_msaa(image, num_samples=4):
     # Konversi gambar ke array NumPy
     img_array = np.array(image)
   
     # Terapkan MSAA dengan melakukan downsampling dan upsampling
     downsampled = img_array[::num_samples, ::num_samples]
     msaa_result = Image.fromarray(downsampled).resize(image.size, Image.BOX)
  
     return msaa_result
  
 # Contoh penggunaan
input_path = "C:\\Users\\Silvy Nur Azkia\\Downloads\\Grafkom\\sebelumMSAA.jpg"
output_path = "msaa_result.jpg"
  
 # Baca gambar menggunakan PIL
input_image = Image.open(input_path)
  
 # Pastikan gambar sudah terpecah menjadi channel warna (misalnya, RGB)
input_image = input_image.convert("RGB")
  
 # Terapkan MSAA
msaa_result = apply_msaa(input_image)
  
 # Simpan hasil
msaa_result.save(output_path)
  
 # Tampilkan hasil
input_image.show(title="Original Image")
msaa_result.show(title="MSAA Result")
