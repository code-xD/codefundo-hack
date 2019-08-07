pragma solidity >=0.4.25 <0.6.0;

contract EVoterVerifier{

    enum StateType{
        L1Verified,
        L2Verified,
        VerifyFailed
    }

    string public voter_name;
    uint64 public aadhar_no;
    uint8 public age;
    uint8 public s_code;
    uint8 public d_code;
    uint8 public c_code;
    uint64 public Pin;
    string public adl_1;
    string public adl_2;
    string public voter_name_template;
    uint64 public aadhar_no_template;
    uint8 public age_template;
    uint8 public s_code_template;
    uint8 public d_code_template;
    uint8 public c_code_template;
    uint64 public Pin_template;
    string public adl_1_template;
    string public adl_2_template;
    StateType public State;

    constructor(string memory v_name,string memory v_name_t,uint8[8] memory long_no,uint64[4] memory main_data,
      string memory add1,string memory add2,string memory add1_t,string memory add2_t) public{
        voter_name=v_name;
        age=long_no[0];
        s_code=long_no[1];
        c_code=long_no[2];
        d_code=long_no[3];
        aadhar_no=main_data[0];
        Pin=main_data[1];
        adl_1=add1;
        adl_2=add2;
        voter_name_template=v_name_t;
        age_template=long_no[4];
        s_code_template=long_no[5];
        c_code_template=long_no[6];
        d_code_template=long_no[7];
        aadhar_no_template=main_data[2];
        Pin_template=main_data[3];
        adl_1_template=add1_t;
        adl_2_template=add2_t;
        State=StateType.L1Verified;
    }

    function VerifyCredentials() public
    {
        if (
            aadhar_no == aadhar_no_template &&
            s_code==s_code_template &&
            c_code==c_code_template &&
            d_code==d_code_template &&
            Pin==Pin_template &&
            age==age_template &&
            keccak256(abi.encodePacked((voter_name))) == keccak256(abi.encodePacked((voter_name_template))) &&
            keccak256(abi.encodePacked((adl_1))) == keccak256(abi.encodePacked((adl_1_template))) &&
            keccak256(abi.encodePacked((adl_2))) == keccak256(abi.encodePacked((adl_2_template)))
            ){
            State=StateType.L2Verified;
        }
        else{
            State=StateType.VerifyFailed;
        }

    }

}
