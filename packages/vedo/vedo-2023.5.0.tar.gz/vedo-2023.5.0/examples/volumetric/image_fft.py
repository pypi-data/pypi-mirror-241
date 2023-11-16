# 2D Fast Fourier Transform of a image
from vedo import Image, show

# url = 'https://comps.canstockphoto.com/a-capital-silhouette-stock-illustrations_csp31110154.jpg'
url = 'https://vedo.embl.es/examples/data/images/dog.jpg'

pic = Image(url).resize([200,None])  # resize so that x has 200 pixels, but keep y aspect-ratio
picfft = pic.fft(logscale=12)
picfft = picfft.tomesh().cmap('Set1',"RGBA").add_scalarbar("12\dotlog(fft)")  # optional step

show([
      [pic, f"Original image\n{url[-40:]}"],
      [picfft, "2D Fast Fourier Transform"],
      [pic.fft(mode='complex').rfft(), "Reversed FFT"],
     ], N=3, bg='gray7', axes=1,
).close()


