// Copyright (c) 2024, Maxim Sysoev and contributors
// For license information, please see license.txt

frappe.ui.form.on("rnokpp-test", {
    refresh(frm) {
        updateRnokppUI(frm);
    },
    rnokpp(frm) {
        updateRnokppUI(frm);
    }
});
function updateRnokppUI(frm) {
    data = rnokppInfo(frm.doc.rnokpp);
    console.log(data);
}
// calculateControlDigit calculates 10th (control digit) from the first 9 digits
function calculateControlDigit(rnokpp) {
    var checksum = rnokpp[0] * -1;
    checksum += rnokpp[1] * 5;
    checksum += rnokpp[2] * 7;
    checksum += rnokpp[3] * 9;
    checksum += rnokpp[4] * 4;
    checksum += rnokpp[5] * 6;
    checksum += rnokpp[6] * 10;
    checksum += rnokpp[7] * 5;
    checksum += rnokpp[8] * 7;

    return (checksum % 11) % 10;
}

function addDays(date, days) {
    var result = new Date(date);
    result.setDate(result.getDate() + days);
    return result;
}
function rnokppInfo(rnokpp) {
    let lengthRnokpp = rnokpp.length;
    console.log(lengthRnokpp);
    if (lengthRnokpp != 10) {
        return
    }
    genderDigit = (rnokpp[8]);  // gender digit
    controlDigit = (rnokpp[9]); // control digit
    calculatedControlDigit = calculateControlDigit(rnokpp);
    console.log(calculatedControlDigit);
    const gender = genderDigit % 2 == 0 ? "Female" : "Male";
    console.log(gender);
    if (controlDigit != calculatedControlDigit) {
        return "ErrInvalidControlDigit";
    }
    numberOfDaysSinceBaseDate = rnokpp[0] * 10000 + rnokpp[1] * 1000 + rnokpp[2] * 100 + rnokpp[3] * 10 + rnokpp[4] * 1
    numberOfDaysSinceBaseDate -= 1;
    birthday = addDays("1900/1/1", numberOfDaysSinceBaseDate);
    return {
        "gender": gender,
        "Birthday": birthday,
    }
}
