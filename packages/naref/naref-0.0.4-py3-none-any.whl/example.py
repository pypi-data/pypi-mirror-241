import naref

from naref.classical.hyper import HyperC
from naref.quantum.hyper import HyperQ
from naref.quantum import QRC
from naref.classical import CRC
from naref import data


qrc = QRC(
	sample_len=2,
	nb_atoms=4,
	N_samples=data.N_samples,
	inp_duration=data.inp_duration,
	reset_rate=data.reset_rate,
	geometry=data.geometry,
	atom_distance=data.atom_distance,
	input_type="sine",
	train_len=data.real_train_len,
	test_len=data.real_test_len,
	verbose=True)
qrc.build_model(data.sine[:250], data.sine[250:280])
qrc.show_test_prediction()
qrc.show_train_prediction()
qer = qrc.get_error_train()
qet = qrc.get_error_test()
crc = CRC(
	sample_len=data.sample_len,
	nb_neurons=data.nb_neurons)
crc.build_model(data.sine[:250], data.sine[250:280])
crc.show_test_prediction()
crc.show_train_prediction()
cer = crc.get_error_train()
cet = crc.get_error_test()

t = QRC()