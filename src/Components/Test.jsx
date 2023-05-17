import { memo } from 'react'

function Test(props) {
    console.log("Test component is called!")
    return (
        <>
            {props.str}
        </>
    );
}

export default memo(Test);