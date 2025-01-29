import qrcode as qr
img=qr.make(qr)
img.save("qr1.png")

print("Image generated successfully and saved as good.png")
