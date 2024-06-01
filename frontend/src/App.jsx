import styles from './App.module.css'
import Profile from '/Profile.svg'
import Language from '/Language.svg'
import Plus from '/Plus.svg'
import Person from '/Person.svg'
import Crest from '/Crest.svg'
import {useEffect, useRef, useState} from "react";
import Crest2 from '/Crest2.svg'
import PlusWhite from '/PlusWhite.svg'
import PlusNew from '/PlusNew.svg'
import ModalFilter from "./ModalFilter.jsx";
import axios from "axios";

function App() {
    const fileInputRef = useRef(null);
    const [serverResponse, setServerResponse] = useState(null);

    const data = {
        "career_profile": [
            {
                "company": "Вымпел, Группа компаний",
                "role": "Старший системный аналитик",
                "period": "май 2023 настоящее время (1 год)",
                "responsibilities": [
                    "Писал документацию в Confluence на редизайн различных страниц.",
                    "Описывал интеграционное взаимодействие загрузки данных на страницу с помощью sequence диаграммы.",
                    "Составлял примерный json-файл данных для контента страницы.",
                    "Проводил ревью других аналитиков.",
                    "Участвовал в переезде со старого монолита на новый микросервис.",
                    "Описывал маппинг полей старого функционала и нового.",
                    "Проверял API в Postman.",
                    "Оформлял подписки на продукт, контролировал выполнение работы."
                ]
            },
            {
                "company": "Сравни.ру, ООО",
                "role": "Младший системный аналитик",
                "period": "март 2023 - май 2023 (3 месяца)",
                "responsibilities": [
                    "Был в команде реферальных программ.",
                    "Частые запросы были от заказчиков, почему не начислился бонус.",
                    "Искал в БД путем джойна и агрегирующих функций за кем зарегистрирован бонус.",
                    "Участвовал в проектировании API по подгрузке дополнительных рекламных акций со сторонних ресурсов.",
                    "Описывал интеграционное взаимодействие (параметры запросов, какими полями должен отдавать запрос, составление спецификации).",
                    "Загружал данные по новым продуктам партнеров в БД, выгружал еженедельный отчет в Excel для заказчика."
                ]
            },
            {
                "company": "Доверенная среда",
                "role": "Младший системный аналитик",
                "period": "март 2022 - январь 2023 (11 месяцев)",
                "responsibilities": [
                    "Интервьюирование заказчика.",
                    "Работа в Bi-системе, настройка загрузки данных, составление отчетов, форм и реестров.",
                    "Строительство дашбордов.",
                    "Участие в ПМИ.",
                    "Проведение ежедневных стендапов, обсуждение того, что делал/будет делать, какие есть блокировщики."
                ]
            },
            {
                "company": "НПО Эшелон, ЗАО",
                "role": "Технический писатель",
                "period": "ноябрь 2021 - март 2022 (5 месяцев)",
                "responsibilities": [
                    "Разработка конструкторской документации: сборочные чертежи на аппаратуру, спецификации.",
                    "Подготовка к испытаниям и сертификации."
                ]
            },
            {
                "company": "НПО Алмаз",
                "role": "Инженер-конструктор"
            }
        ]
    };



    const [skills, setSkills] = useState(['Python', 'Celery']);

    const [selectedJob, setSelectedJob] = useState('');
    const [showDropdown, setShowDropdown] = useState(false);
    const [experiences, setExperiences] = useState([]);
    const jobs = ['Backend Developer', 'Frontend Developer', 'System Analyst'];
    const [hardSkills, setHardSkills] = useState(['Python', 'SQL', 'MongoDB', 'Celery']);
    const [softSkills, setSoftSkills] = useState([]);
    const [isHardSkillsModalOpen, setHardSkillsModalOpen] = useState(false);
    const [isSoftSkillsModalOpen, setSoftSkillsModalOpen] = useState(false);
    const [isExperiencesModalOpen, setExperiencesModalOpen] = useState(false);
    const [newSkill, setNewSkill] = useState('');
    const [newExperience, setNewExperience] = useState('');
    const [modalActive, setModalActive] = useState(false);


    useEffect(() => {

    }, []);

    const handleFileChange = async () => {
        const file = fileInputRef.current.files[0];
        const formData = new FormData();
        formData.append('file', file);
        try {
            const response = await axios.post('/your-server-endpoint', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            setServerResponse(response.data);
        } catch (error) {
            console.error('Ошибка при отправке файла:', error);
        }
    };


    useEffect(() => {
        setNewSkill([...hardSkills, ...softSkills]);
    }, [hardSkills, softSkills]);

    const getSkillClass = (skill) => {
        if (newSkill.includes(skill) && !skills.includes(skill)) {
            return styles.redSkill;
        } else if (newSkill.includes(skill)) {
            return styles.greenSkill;
        }
        return styles.greySkill;
    };


    const toggleDropdown = () => {
        setShowDropdown(!showDropdown);
    };

    const handleJobSelect = (job) => {
        setSelectedJob(job);
        setShowDropdown(false);
    };

    const handleUploadClick = () => {
        fileInputRef.current.click();
    };

    const summaries = [
        {name: 'Тестович Тест Тестович', role: 'Frontend developer', match: 89, description:"Новые делишки, новые хуишки" },
    ];


    const handleAddHardSkill = () => {
        if (newSkill && !hardSkills.includes(newSkill)) {
            setHardSkills([...hardSkills, newSkill]);
            setNewSkill('');
            setHardSkillsModalOpen(false);
        }
    };

    const handleAddSoftSkill = () => {
        if (newSkill && !softSkills.includes(newSkill)) {
            setSoftSkills([...softSkills, newSkill]);
            setNewSkill('');
            setSoftSkillsModalOpen(false);
        }
    };

    const getMatchClass = (match) => {
        if (match > 70) {
            return styles.green;
        } else if (match > 40) {
            return styles.yellow;
        } else {
            return styles.red;
        }
    };

    const handleAddExperience = () => {
        if (newExperience && !experiences.includes(newExperience)) {
            setExperiences([...experiences, newExperience]);
            setNewExperience('');
            setExperiencesModalOpen(false);
        }
    };

    const handleRemoveExperience = (experience) => {
        setExperiences(experiences.filter(e => e !== experience));
    };

    const handleRemoveHardSkill = (skill) => {
        setHardSkills(hardSkills.filter(s => s !== skill));
    };

    const handleRemoveSoftSkill = (skill) => {
        setSoftSkills(softSkills.filter(s => s !== skill));
    };

    return (
        <div className={styles.MainContainer}>
            <div className={styles.HeaderContainer}>
                <img src={Language} width={100}></img>
                <img src={Profile} width={100}></img>
            </div>
            <div className={styles.BodyContainer}>
                <div className={styles.NameOfContainer}>Load files</div>
                <div className={styles.BodyContainerWithBorder}>
                    <div className={styles.UploadAndSearchContainer}>
                        <button className={styles.ButtonUpload} onClick={handleUploadClick}>Upload summary file<img
                            src={Plus}></img></button>
                        <input type={'file'} className={styles.input} ref={fileInputRef} onChange={handleFileChange} ></input>
                        <input className={styles.Search} placeholder={'Search'}></input>
                    </div>
                    <div className={styles.TotalSummaries}>
                        Total summaries: {summaries.length}
                    </div>
                    {summaries.length > 0 ? (
                        summaries.map((summary, index) => (
                            <div key={index} className={styles.summaryItem}>
                                <div className={styles.ContainerOfCandidate}>
                                    <img src={Person} width={50}></img>
                                    <div className={styles.summaryName}>{summary.name}</div>
                                    <div
                                        className={`${styles.summaryRole} ${summary.role.includes('Backend') ? styles.backend : styles.frontend}`}>
                                        {summary.role}
                                    </div>
                                    <img src={Crest} className={styles.Crest}></img>
                                </div>
                            </div>
                        ))
                    ) : (
                        <div className={styles.NoSummariesMessage}>
                            Пока нет кандидатов
                        </div>
                    )}
                    <div className={styles.More}>
                        <div className={styles.Circle}></div>
                        <div className={styles.Circle}></div>
                        <div className={styles.Circle}></div>
                    </div>
                </div>
                <div className={styles.NameOfContainer}>Create Template</div>
                <div className={styles.BodyContainerWithoutBorder}>
                    <div className={styles.Template}>
                        <div className={styles.savedTemplate}>Saved Templates <img src={Plus}></img></div>
                        <img src={Crest2} width={70}></img>
                    </div>
                    <div className={styles.Person}>
                        <div className={styles.DropDownMenu}>
                            <button onClick={toggleDropdown} className={styles.ButtonText}>
                                {selectedJob ? selectedJob : 'Выберите профессию'}
                            </button>
                            {showDropdown && (
                                <div className={styles.ButtonTextProps}>
                                    {jobs.map((job, index) => (
                                        <a key={index} onClick={() => handleJobSelect(job)}>
                                            {job}
                                        </a>
                                    ))}
                                </div>
                            )}
                        </div>
                    </div>
                    <div className={styles.HardSkills}>
                        <div className={styles.HardSkillsName}>Hard Skills</div>
                        <div className={styles.skillList}>
                            <div className={styles.skills}>
                                {hardSkills.map(skill => (
                                    <div key={skill} className={styles.skillItem}>
                                        {skill}
                                        <button onClick={() => handleRemoveHardSkill(skill)}
                                                className={styles.removeButton}>
                                            <img src={PlusNew} width={30} height={30}
                                                 className={styles.removeButtonIcon} alt="Remove"/>
                                        </button>
                                    </div>
                                ))}
                                <button onClick={() => setHardSkillsModalOpen(true)} className={styles.addButton}>
                                    <img src={PlusWhite} width={70} alt="Add"/>
                                </button>
                            </div>
                        </div>
                        {isHardSkillsModalOpen && (
                            <div className={styles.modal}>
                                <input
                                    type="text"
                                    value={newSkill}
                                    onChange={(e) => setNewSkill(e.target.value)}
                                    placeholder="Enter skill"
                                />
                                <button onClick={handleAddHardSkill}>Add Skill</button>
                                <button onClick={() => setHardSkillsModalOpen(false)}>Close</button>
                            </div>
                        )}
                    </div>
                    <div className={styles.SoftSkills}>
                        <div className={styles.SoftSkillsName}>Soft Skills</div>
                        <div className={styles.skillList}>
                            <div className={styles.skills}>
                                {softSkills.map(skill => (
                                    <div key={skill} className={styles.skillItem}>
                                        {skill}
                                        <button onClick={() => handleRemoveSoftSkill(skill)}
                                                className={styles.removeButton}>
                                            <img src={PlusNew} width={30} height={30}
                                                 className={styles.removeButtonIcon} alt="Remove"/>
                                        </button>
                                    </div>
                                ))}
                                <button onClick={() => setSoftSkillsModalOpen(true)} className={styles.addButton}>
                                    <img src={PlusWhite} width={70} alt="Add"/>
                                </button>
                            </div>
                        </div>
                        {isSoftSkillsModalOpen && (
                            <div className={styles.modalPlus}>
                                <input
                                    type="text"
                                    value={newSkill}
                                    onChange={(e) => setNewSkill(e.target.value)}
                                    placeholder="Enter skill"
                                />
                                <button onClick={handleAddSoftSkill}>Add Skill</button>
                                <button onClick={() => setSoftSkillsModalOpen(false)}>Close</button>
                            </div>
                        )}
                    </div>
                    <div className={styles.Experience}>
                        <div className={styles.ExperienceName}>Experience</div>
                        <div className={styles.experienceList}>
                            <div className={styles.experiences}>
                                {experiences.map(experience => (
                                    <div key={experience} className={styles.skillItem}>
                                        {experience}
                                        <button onClick={() => handleRemoveExperience(experience)}
                                                className={styles.removeButton}>
                                            <img src={PlusNew} width={30} height={30}
                                                 className={styles.removeButtonIcon} alt="Remove"/>
                                        </button>
                                    </div>
                                ))}
                                <button onClick={() => setExperiencesModalOpen(true)} className={styles.addButton}>
                                    <img src={PlusWhite} width={70} alt="Add"/>
                                </button>
                            </div>
                        </div>
                        {isExperiencesModalOpen && (
                            <div className={styles.modalPlusPlus}>
                                <input
                                    type="text"
                                    value={newExperience}
                                    onChange={(e) => setNewExperience(e.target.value)}
                                    placeholder="Enter experience"
                                />
                                <button onClick={handleAddExperience}>Add Experience</button>
                                <button onClick={() => setExperiencesModalOpen(false)}>Close</button>
                            </div>
                        )}
                    </div>
                </div>
                <button className={styles.Analyse}>Analyse</button>
                <div className={styles.NameOfResultContainer}>
                    <div className={styles.Result}>Result Search</div>
                    <input className={styles.Search} placeholder={'Search'}></input>
                </div>
                <div className={styles.resultContainerWithoutBorder}>
                    <div className={styles.TotalSummaries}>
                        Name
                    </div>
                    {summaries.length > 0 ? (
                        summaries.map((summary, index) => (
                            <div key={index} className={styles.summaryItem} onClick={() =>setModalActive(true)}>
                                <div className={styles.ContainerOfCandidateNew}>
                                    <img src={Person} width={50}></img>
                                    <div className={styles.summaryName}>{summary.name}</div>
                                    <div
                                        className={`${styles.Match} ${getMatchClass(summary.match)}`}>{summary.match}%
                                    </div>
                                </div>
                            </div>
                        ))
                    ) : (
                        <div className={styles.NoSummariesMessage}>
                            Пока нет кандидатов
                        </div>
                    )}
                    <div className={styles.More}>
                        <div className={styles.Circle}></div>
                        <div className={styles.Circle}></div>
                        <div className={styles.Circle}></div>
                    </div>
                </div>
            </div>
            <ModalFilter active={modalActive} setActive={() => setModalActive(false)}>
                <div className={styles.Border}>
                    {summaries.length > 0 ? (
                        summaries.map((summary, index) => (
                            <div key={index} className={styles.PersonItem}>
                                <div className={styles.PersonExpirience}>
                                    <img src={Person} width={100}></img>
                                    <div className={styles.summaryName}>{summary.name}<p>{summary.role}</p></div>
                                </div>
                                <div className={styles.MatchPerson}>Template Match <div
                                    className={`${styles.Match} ${getMatchClass(summary.match)}`}>{summary.match}%
                                </div></div>
                                <div className={styles.Skills}>
                                    Skills
                                    <div className={styles.SkillsMap}>
                                        {skills.map((skill, index) => (
                                            <div key={index} className={getSkillClass(skill)}>
                                                {skill}
                                            </div>
                                        ))}
                                    </div>
                                </div>
                                <div className={styles.MatchPerson}>
                                    Past
                                </div>
                                <div className={styles.BorderForPast}>
                                    <div style={{padding: '20px', fontFamily: 'Arial, sans-serif', color: 'white'}}>
                                        {data.career_profile.map((job, index) => (
                                            <div key={index} style={{marginBottom: '20px'}}>
                                                <h2>{job.role} @ {job.company}</h2>
                                                <p><strong>Period:</strong> {job.period}</p>
                                                <div style={{marginLeft: '20px'}}>
                                                    <p><strong>Responsibilities:</strong></p>
                                                    <ul>
                                                        {job.responsibilities && job.responsibilities.map((responsibility, index) => (
                                                            <li key={index}>{responsibility}</li>
                                                        ))}
                                                    </ul>
                                                </div>
                                            </div>
                                        ))}
                                    </div>
                                </div>
                                <div className={styles.MatchPerson}>
                                    Career Profile
                                </div>
                                <div className={styles.CarrearProfile}>

                                </div>
                                <button className={styles.LoadInCSV}>Load in CSV</button>
                            </div>
                        ))
                    ) : (
                        <div className={styles.NoSummariesMessage}>
                            Пока нет кандидатов
                        </div>
                    )}
                </div>
            </ModalFilter>
        </div>
    )
}

export default App
