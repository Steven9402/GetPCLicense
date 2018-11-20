#include <idmodule.cpp>
#include <iostream>
using namespace std;
int main(){
    pc_id pcid_impl;

    if(!pcid_impl.calc_cpu_id_by_asm())cout<<"can not calc cpu id"<<endl;
    else{
        string cpuid = pcid_impl.get_cpu_id();
        cout<< "cpu_id_by_asm: "<<cpuid<<endl;
    }

    if(!pcid_impl.calc_mac_address_by_ioctl())cout<<"can not get mac id"<<endl;
    else{
        string mac_id=pcid_impl.get_mac_address();
        cout<< "mac_address: "<<mac_id<<endl;
    }

    if(!pcid_impl.calc_disk_serial_number())cout<<"can not get disk serial number"<<endl;
    else{
        string disk_serial_number=pcid_impl.get_disk_serial_number();
        cout<< "disk_serial_number: "<<disk_serial_number<<endl;
    }
    
    return 1;

}
