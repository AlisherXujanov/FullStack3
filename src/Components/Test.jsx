import { memo } from 'react'
import { useEffect } from 'react';

function Test(props) {
    useEffect(() => {
        console.log("Test component is rendered");
    })

    return (
        <>
            {props.str}
        </>
    );
}

export default memo(Test);