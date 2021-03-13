window.addEventListener('load', () => {
const showUnits = () => {
        const firstUnit = document.getElementById('id_first_unit');
        const secondUnit = document.getElementById('id_second_unit');
        var showUnitOne = document.getElementById('show-unit-1');
        var showUnitTwo= document.getElementById('show-unit-2');

        showUnitOne.innerText = firstUnit.value;
        showUnitTwo.innerText = secondUnit.value;


        firstUnit.addEventListener('change', () => {
            showUnitOne.innerText = firstUnit.value;
        });
        secondUnit.addEventListener('change', () => {
            showUnitTwo.innerText = secondUnit.value;
        });
    }

    showUnits();
});

