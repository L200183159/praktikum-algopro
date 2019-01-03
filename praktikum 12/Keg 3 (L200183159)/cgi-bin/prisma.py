def segiempat():
	luas = 6 * 4
	return luas
print "<!DOCTYPE html>"
print
print """<html>
	<head>
		<title>Luas Prisma</title>
	</head>
	<body>
		<form>
			<table>
				<tr>
					<td rowspan='8'>
					<img src='../prisma.jpg' width='160' height='160'>
					</td>
					<td>
						<p><b><font size='5'>Bangun Geometri</font></b></p>
					</td>
				</tr>
				
				<tr>
					<td>Nama Bangun</td>
					<td>:</td>
					<td>Prisma</td>
				</tr>
				
				<tr>
					<td>Dimensi</td>
					<td>:</td>
					<td>3D</td>
				</tr>
				
				<tr>
					<td>Rumus Luas</td>
					<td>:</td>
					<td>((a x t) x 2) + (kel.a x t)</td>
				</tr>
				
				<tr>
					<td>Sisi</td>
					<td>:</td>
					<td>
					5
					</td>
				</tr>
				
    
				<tr>
					<td>Luas</td>
					<td>:</td>
					<td>"""
print prisma()
print"""</td>
				</tr>
			</table>
		</form>
	</body>
</html>"""