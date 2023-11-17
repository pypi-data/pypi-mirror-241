"""
Example script converting records from PhysioNet into Muse XML files.

Files are chosen to create a varied dataset of 10 records, including:

- Common and uncommon sampling frequencies (125, 250, 257, 500, 1000)
- Varied number of channels (8, 12)
- Varied signal length (10s, 15s)
- Pathologies (normal, arrhythmia, myocardial infarction)

The output files are saved in the same directory as the input files.
"""
import os
import numpy as np
from pathlib import Path

import wfdb
from ecghelper.waveform import WaveformRecord

def main():
    # we use the wfdb library to read specific files from PhysioNet directly

    # ecg-arrhythmia/1.0.0
    #   WFDBRecords/03/032/JS02292 - female, bradycardia, low QRS voltage, 500 Hz, 10s
    #   WFDBRecords/04/041/JS03244 - male, afib, left ventricular hypertrophy, 500 Hz, 10s

    # incartdb/1.0.0/
    #   I06 - male, 80, Transient ischemic attack, 257 Hz, 30 minutes
    #   I12 - female, 39, ventricular couplets, ST couplets, 257 Hz, 30 minutes

    # ptb-xl/1.0.3/
    #   01365_lr - 100 Hz, 10s
    #   00001_hr - 500 Hz, 10s
    #   00001_hr_250 - downsampled to 250 Hz, 10s
    #   00002_hr - 500 Hz, 10s
    #   00002_hr_250 - downsampled to 250 Hz, 10s

    # mhd-effect-ecg-mri/1.0.0/
    #   ECGMRI3T05Ff - male, 29, no dx, 1024 Hz, 490s
    #   ECGMRI7T04Ff - female, 29, no dx, 1024 Hz, 326s

    # mimic-iv-ecg/1.0/
    #   p1003/p10030630/s43199371/43199371 - female, 83, afib, 500 Hz, 10s
    #   p1003/p10030753/s40735970/40735970 - female, 47, old MI, 500 Hz, 10s

    # norwegian-athlete-ecg/1.0.0/
    #   ath_003 - male, 25, left axis deviation (normal ECG), 500 Hz, 10s
    #   ath_008 - male, 25, incomplete RBBB, 500 Hz, 10s
    #   ath_016 - male, 25, normal ECG, 500 Hz, 10s

    # ecgdmmld/1.0.0/
    #   raw/2001/EC4F786C-3D52-4291-A180-4F9F65B84A14 - male, 21, dosed with Moxifloxacin + Diltiazem, 1000Hz, 10s
    record_list = [
        {'record_path': 'WFDBRecords/03/032/JS02292', 'db': 'ecg-arrhythmia/1.0.0'},
        {'record_path': 'WFDBRecords/04/041/JS03244', 'db': 'ecg-arrhythmia/1.0.0'},
        {'record_path': 'I06', 'db': 'incartdb/1.0.0'},
        {'record_path': 'I12', 'db': 'incartdb/1.0.0'},
        {'record_path': '00001_hr', 'db': 'ptb-xl/1.0.3'},
        {'record_path': '00001_hr_250', 'db': 'ptb-xl/1.0.3'},
        {'record_path': '00002_hr', 'db': 'ptb-xl/1.0.3'},
        {'record_path': '00002_hr_250', 'db': 'ptb-xl/1.0.3'},
        {'record_path': 'ECGMRI3T05Ff', 'db': 'mhd-effect-ecg-mri/1.0.0'},
        {'record_path': 'ECGMRI7T04Ff', 'db': 'mhd-effect-ecg-mri/1.0.0'},
        {'record_path': 'p1003/p10030630/s43199371/43199371', 'db': 'mimic-iv-ecg/1.0'},
        {'record_path': 'p1003/p10030753/s40735970/40735970', 'db': 'mimic-iv-ecg/1.0'},
        {'record_path': 'ath_003', 'db': 'norwegian-athlete-ecg/1.0.0'},
        {'record_path': 'ath_008', 'db': 'norwegian-athlete-ecg/1.0.0'},
        {'record_path': 'ath_016', 'db': 'norwegian-athlete-ecg/1.0.0'},
        {'record_path': 'raw/2001/EC4F786C-3D52-4291-A180-4F9F65B84A14', 'db': 'ecgdmmld/1.0.0'}
    ]
    for record_info in record_list:
        # parse the record names so that they work with wfdb tools
        source_db = record_info['db']
        source_record = record_info['record_path']
        source_db = source_db.rstrip('/')

        # create the record name
        if '/' in source_record:
            source_record_name = source_record.split('/')[-1]
            pn_dir = '/'.join([source_db] + source_record.split("/")[:-1])
        else:
            source_record_name = source_record
            pn_dir = source_db
        
        record_info['record_name'] = source_record_name
        record_info['pn_dir'] = pn_dir
    

    # now download records
    for record_info in record_list:
        print(pn_dir)
        record = wfdb.rdrecord(source_record_name, pn_dir=pn_dir)
        # output to ./data folder
        record_name = record_info['record_name']
        output_dir = Path('tests/data/sample').resolve()
        output_dir.mkdir(parents=True, exist_ok=True)
        record.wrsamp(output_dir / record_name)

if __name__ == '__main__':
    main()

def stuff_todo():
    files = data_path.glob('*.hea')
    filenames = [x.stem for x in files][:10]

    for filename in filenames:
        # read in the WFDB format record
        record = WaveformRecord.from_wfdb(data_path / f"{filename}")

        fcns = [
            (".xml", record.to_xml, WaveformRecord.from_xml),
            # TODO: edf is failing!
            # (".edf", record.to_edf, WaveformRecord.from_edf),
            (".csv", record.to_csv, WaveformRecord.from_csv),
        ]
        for ext, to_fcn, load_fcn in fcns:
            # precision for these records is 5 digits
            # rounding is useful for output to EDF, CSV, etc.
            signal = np.around(record.data, 5)

            output_file = Path(data_path / f'{filename}{ext}')
            to_fcn(output_file)
            assert os.path.exists(output_file)

            # re-load, compare to original signal
            record_reloaded = load_fcn(output_file)
            signal_reloaded = record_reloaded.data
            assert signal_reloaded.shape == signal.shape

            # assert approximately equal
            assert (abs(signal_reloaded - signal) < 0.01).all()

            assert signal_reloaded.shape[0] > 0
            assert signal_reloaded.shape[1] == 12

            # reloaded signal should be very close
            np.allclose(signal_reloaded, signal, atol=0.0001)
