import "./ModalFilter.css"
import {Transition } from "react-transition-group"

const ModalFilter = ({active, setActive, children}) => {
    const onWrapperClick = (event) => {
        if(event.target.classList.contains("modalWrapper")) setActive()
    }
    return (
        <>
            <Transition in={active} timeout={350} unmountOnExit={true}>
                {(state) => (
                    <div className={`modal modal--${state}`}>
                        <div className='modalWrapper' onClick={onWrapperClick}>
                            <div className='contentModal' onClick={e => e.stopPropagation()}>
                                {children}
                            </div>
                        </div>
                    </div>
                )}
            </Transition>
        </>
    )
}

export default ModalFilter;