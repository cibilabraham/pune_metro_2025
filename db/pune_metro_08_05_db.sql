--
-- PostgreSQL database dump
--

-- Dumped from database version 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: admin_tools_stats_criteriatostatsm2m; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.admin_tools_stats_criteriatostatsm2m (
    id integer NOT NULL,
    "order" integer,
    prefix character varying(255) NOT NULL,
    use_as character varying(90) NOT NULL,
    criteria_id integer NOT NULL,
    stats_id integer NOT NULL,
    CONSTRAINT admin_tools_stats_criteriatostatsm2m_order_check CHECK (("order" >= 0))
);


ALTER TABLE public.admin_tools_stats_criteriatostatsm2m OWNER TO postgres;

--
-- Name: admin_tools_stats_criteriatostatsm2m_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.admin_tools_stats_criteriatostatsm2m_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.admin_tools_stats_criteriatostatsm2m_id_seq OWNER TO postgres;

--
-- Name: admin_tools_stats_criteriatostatsm2m_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.admin_tools_stats_criteriatostatsm2m_id_seq OWNED BY public.admin_tools_stats_criteriatostatsm2m.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    role integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: COLUMN auth_user.role; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.auth_user.role IS 'user role';


--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: dash_stats_criteria; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dash_stats_criteria (
    id integer NOT NULL,
    criteria_name character varying(90) NOT NULL,
    criteria_fix_mapping jsonb,
    dynamic_criteria_field_name character varying(90),
    criteria_dynamic_mapping jsonb,
    created_date timestamp with time zone NOT NULL,
    updated_date timestamp with time zone NOT NULL
);


ALTER TABLE public.dash_stats_criteria OWNER TO postgres;

--
-- Name: dash_stats_criteria_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dash_stats_criteria_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dash_stats_criteria_id_seq OWNER TO postgres;

--
-- Name: dash_stats_criteria_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dash_stats_criteria_id_seq OWNED BY public.dash_stats_criteria.id;


--
-- Name: dashboard_stats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_stats (
    id integer NOT NULL,
    graph_key character varying(90) NOT NULL,
    graph_title character varying(90) NOT NULL,
    model_app_name character varying(90) NOT NULL,
    model_name character varying(90) NOT NULL,
    date_field_name character varying(90) NOT NULL,
    operation_field_name character varying(90),
    type_operation_field_name character varying(90),
    is_visible boolean NOT NULL,
    created_date timestamp with time zone NOT NULL,
    updated_date timestamp with time zone NOT NULL,
    user_field_name character varying(90),
    default_chart_type character varying(90) NOT NULL,
    default_time_period integer NOT NULL,
    default_time_scale character varying(90) NOT NULL,
    y_axis_format character varying(90),
    "distinct" boolean NOT NULL,
    CONSTRAINT dashboard_stats_default_time_period_check CHECK ((default_time_period >= 0))
);


ALTER TABLE public.dashboard_stats OWNER TO postgres;

--
-- Name: dashboard_stats_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_stats_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_stats_id_seq OWNER TO postgres;

--
-- Name: dashboard_stats_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_stats_id_seq OWNED BY public.dashboard_stats.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: fracas_action; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_action (
    action_id integer NOT NULL,
    action_description character varying(550) NOT NULL,
    action_owner character varying(550) NOT NULL,
    action_status character varying(550) NOT NULL,
    action_due_date date,
    progress_log text NOT NULL,
    defect_discussion_id_id integer
);


ALTER TABLE public.fracas_action OWNER TO postgres;

--
-- Name: fracas_action_action_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_action_action_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_action_action_id_seq OWNER TO postgres;

--
-- Name: fracas_action_action_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_action_action_id_seq OWNED BY public.fracas_action.action_id;


--
-- Name: fracas_asset; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_asset (
    id integer NOT NULL,
    asset_config_id character varying(550) NOT NULL,
    location_id text NOT NULL,
    location_description text NOT NULL,
    asset_serial_number character varying(550) NOT NULL,
    asset_type integer NOT NULL,
    asset_description text NOT NULL,
    software_version character varying(550) NOT NULL,
    software_description text NOT NULL,
    asset_status character varying(550) NOT NULL,
    is_active integer NOT NULL,
    "P_id" integer NOT NULL,
    sub_location text
);


ALTER TABLE public.fracas_asset OWNER TO postgres;

--
-- Name: fracas_asset_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_asset_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_asset_id_seq OWNER TO postgres;

--
-- Name: fracas_asset_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_asset_id_seq OWNED BY public.fracas_asset.id;


--
-- Name: fracas_assetregister; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_assetregister (
    id integer NOT NULL
);


ALTER TABLE public.fracas_assetregister OWNER TO postgres;

--
-- Name: fracas_assetregister_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_assetregister_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_assetregister_id_seq OWNER TO postgres;

--
-- Name: fracas_assetregister_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_assetregister_id_seq OWNED BY public.fracas_assetregister.id;


--
-- Name: fracas_assetserialnumberids; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_assetserialnumberids (
    uid_id integer NOT NULL,
    asset_type character varying(550),
    location_id character varying(550),
    sub_location character varying(550),
    last_id integer NOT NULL
);


ALTER TABLE public.fracas_assetserialnumberids OWNER TO postgres;

--
-- Name: fracas_assetserialnumberids_uid_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_assetserialnumberids_uid_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_assetserialnumberids_uid_id_seq OWNER TO postgres;

--
-- Name: fracas_assetserialnumberids_uid_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_assetserialnumberids_uid_id_seq OWNED BY public.fracas_assetserialnumberids.uid_id;


--
-- Name: fracas_correctiveaction; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_correctiveaction (
    corrective_action_id integer NOT NULL,
    corrective_action_owner character varying(550) NOT NULL,
    corrective_action_description text NOT NULL,
    corrective_action_update text NOT NULL,
    corrective_action_status character varying(550) NOT NULL,
    defect_id integer NOT NULL,
    "P_id" integer NOT NULL,
    is_active integer NOT NULL
);


ALTER TABLE public.fracas_correctiveaction OWNER TO postgres;

--
-- Name: fracas_correctiveaction_corrective_action_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_correctiveaction_corrective_action_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_correctiveaction_corrective_action_id_seq OWNER TO postgres;

--
-- Name: fracas_correctiveaction_corrective_action_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_correctiveaction_corrective_action_id_seq OWNED BY public.fracas_correctiveaction.corrective_action_id;


--
-- Name: fracas_defect; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_defect (
    start_date date,
    end_date date,
    asset_type character varying(550) NOT NULL,
    defect_id integer NOT NULL,
    defect_description text NOT NULL,
    defect_open_date date,
    defect_closed_date date,
    investigation text NOT NULL,
    defect_status character varying(550) NOT NULL,
    defect_status_remarks text NOT NULL,
    oem_defect_reference text NOT NULL,
    oem_target_date date,
    "P_id" integer NOT NULL,
    is_active integer NOT NULL
);


ALTER TABLE public.fracas_defect OWNER TO postgres;

--
-- Name: fracas_defect_defect_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_defect_defect_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_defect_defect_id_seq OWNER TO postgres;

--
-- Name: fracas_defect_defect_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_defect_defect_id_seq OWNED BY public.fracas_defect.defect_id;


--
-- Name: fracas_defectdiscussion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_defectdiscussion (
    defect_discussion_id integer NOT NULL,
    meeting_date date,
    defect_id integer,
    review_board_id integer NOT NULL,
    description character varying(550) NOT NULL
);


ALTER TABLE public.fracas_defectdiscussion OWNER TO postgres;

--
-- Name: fracas_defectdiscussion_attendees; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_defectdiscussion_attendees (
    id integer NOT NULL,
    defectdiscussion_id integer NOT NULL,
    userprofile_id integer NOT NULL
);


ALTER TABLE public.fracas_defectdiscussion_attendees OWNER TO postgres;

--
-- Name: fracas_defectdiscussion_attendees_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_defectdiscussion_attendees_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_defectdiscussion_attendees_id_seq OWNER TO postgres;

--
-- Name: fracas_defectdiscussion_attendees_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_defectdiscussion_attendees_id_seq OWNED BY public.fracas_defectdiscussion_attendees.id;


--
-- Name: fracas_defectdiscussion_defect_discussion_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_defectdiscussion_defect_discussion_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_defectdiscussion_defect_discussion_id_seq OWNER TO postgres;

--
-- Name: fracas_defectdiscussion_defect_discussion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_defectdiscussion_defect_discussion_id_seq OWNED BY public.fracas_defectdiscussion.defect_discussion_id;


--
-- Name: fracas_eirgeneration; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_eirgeneration (
    eir_id integer NOT NULL,
    depot character varying(550),
    addressed_by text,
    incident_details text,
    repercussion text,
    incident_location character varying(550),
    incident_time character varying(550),
    failure_id_id integer,
    eir_gen_id character varying(550),
    component text,
    action_taken_in_depot text,
    concern text,
    further_action text,
    "TRSL" character varying(550),
    signature_img2 text,
    signature_img3 text
);


ALTER TABLE public.fracas_eirgeneration OWNER TO postgres;

--
-- Name: fracas_eirids; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_eirids (
    uid_id integer NOT NULL,
    year character varying(550),
    last_id integer NOT NULL
);


ALTER TABLE public.fracas_eirids OWNER TO postgres;

--
-- Name: fracas_eirids_uid_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_eirids_uid_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_eirids_uid_id_seq OWNER TO postgres;

--
-- Name: fracas_eirids_uid_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_eirids_uid_id_seq OWNED BY public.fracas_eirids.uid_id;


--
-- Name: fracas_eirimages; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_eirimages (
    img_id integer NOT NULL,
    file_path text,
    is_active integer NOT NULL,
    eir_dt_id_id integer
);


ALTER TABLE public.fracas_eirimages OWNER TO postgres;

--
-- Name: fracas_eirimages_img_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_eirimages_img_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_eirimages_img_id_seq OWNER TO postgres;

--
-- Name: fracas_eirimages_img_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_eirimages_img_id_seq OWNED BY public.fracas_eirimages.img_id;


--
-- Name: fracas_employeemaster; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_employeemaster (
    id integer NOT NULL,
    employee_id character varying(550),
    name character varying(550) NOT NULL,
    designation character varying(550) NOT NULL
);


ALTER TABLE public.fracas_employeemaster OWNER TO postgres;

--
-- Name: fracas_employeemaster_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_employeemaster_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_employeemaster_id_seq OWNER TO postgres;

--
-- Name: fracas_employeemaster_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_employeemaster_id_seq OWNED BY public.fracas_employeemaster.id;


--
-- Name: fracas_failuredata; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_failuredata (
    id integer NOT NULL,
    failure_id character varying(600),
    event_description character varying(600) NOT NULL,
    date date NOT NULL,
    "time" time without time zone NOT NULL,
    detection character varying(600) NOT NULL,
    service_delay character varying(600),
    immediate_investigation text NOT NULL,
    failure_type character varying(600),
    safety_failure character varying(550) NOT NULL,
    hazard_id character varying(550),
    cm_description text NOT NULL,
    replaced_asset_config_id character varying(500) NOT NULL,
    cm_start_date date NOT NULL,
    cm_start_time time without time zone NOT NULL,
    cm_end_date date,
    cm_end_time time without time zone,
    oem_failure_reference text NOT NULL,
    asset_config_id_id character varying(550) NOT NULL,
    defect_id integer,
    mode_description character varying(600),
    mode_id_id integer,
    asset_type character varying(550) NOT NULL,
    "P_id" integer NOT NULL,
    is_active integer NOT NULL,
    "TO_name" text,
    department character varying(550),
    direction text,
    equipment text,
    kilometre_reading character varying(550),
    location text,
    location_id character varying(550),
    no_of_trip_cancel integer NOT NULL,
    "reported_to_PPIO" character varying(550),
    sel_car text,
    incident character varying(550),
    deboarding character varying(550)
);


ALTER TABLE public.fracas_failuredata OWNER TO postgres;

--
-- Name: fracas_failuredata_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_failuredata_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_failuredata_id_seq OWNER TO postgres;

--
-- Name: fracas_failuredata_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_failuredata_id_seq OWNED BY public.fracas_failuredata.id;


--
-- Name: fracas_failuredataids; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_failuredataids (
    uid_id integer NOT NULL,
    year character varying(550),
    month character varying(550),
    last_id integer NOT NULL
);


ALTER TABLE public.fracas_failuredataids OWNER TO postgres;

--
-- Name: fracas_failuredataids_uid_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_failuredataids_uid_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_failuredataids_uid_id_seq OWNER TO postgres;

--
-- Name: fracas_failuredataids_uid_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_failuredataids_uid_id_seq OWNED BY public.fracas_failuredataids.uid_id;


--
-- Name: fracas_failuremode; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_failuremode (
    id integer NOT NULL,
    mode_id character varying(550) NOT NULL,
    asset_type character varying(255)[] NOT NULL,
    end_date date,
    start_date date,
    mode_description character varying(550),
    "P_id" integer NOT NULL,
    is_active integer NOT NULL
);


ALTER TABLE public.fracas_failuremode OWNER TO postgres;

--
-- Name: fracas_failuremode_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_failuremode_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_failuremode_id_seq OWNER TO postgres;

--
-- Name: fracas_failuremode_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_failuremode_id_seq OWNED BY public.fracas_failuremode.id;


--
-- Name: fracas_history; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_history (
    id integer NOT NULL,
    "P_id" integer NOT NULL,
    date date,
    message text NOT NULL,
    "time" time without time zone,
    user_id integer NOT NULL,
    function_name character varying(50)
);


ALTER TABLE public.fracas_history OWNER TO postgres;

--
-- Name: fracas_history_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_history_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_history_id_seq OWNER TO postgres;

--
-- Name: fracas_history_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_history_id_seq OWNED BY public.fracas_history.id;


--
-- Name: fracas_investigationdetails; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_investigationdetails (
    details_id integer NOT NULL,
    non_compliance_details text,
    onvestigation_details text,
    "relevant_ERTS_clause" text,
    is_active integer NOT NULL,
    eir_dt_id_id integer
);


ALTER TABLE public.fracas_investigationdetails OWNER TO postgres;

--
-- Name: fracas_investigationdetails_details_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_investigationdetails_details_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_investigationdetails_details_id_seq OWNER TO postgres;

--
-- Name: fracas_investigationdetails_details_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_investigationdetails_details_id_seq OWNED BY public.fracas_investigationdetails.details_id;


--
-- Name: fracas_jobcard; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_jobcard (
    job_id integer NOT NULL,
    train_set_no character varying(550),
    date date,
    "time" time without time zone,
    department character varying(550),
    subsystem character varying(550) NOT NULL,
    equipment text,
    job_description text,
    nature_of_job text,
    sic_required text,
    assigned_to text,
    last_update date,
    status integer NOT NULL,
    job_card_no character varying(550) NOT NULL,
    run_status integer NOT NULL,
    ohe_required character varying(550) NOT NULL,
    issued_to text,
    completion_time character varying(550) NOT NULL,
    from_revenue_service character varying(550) NOT NULL,
    delay_to_service character varying(550) NOT NULL,
    trip_no character varying(550) NOT NULL,
    event_date date,
    event_time time without time zone,
    sic_no character varying(550) NOT NULL,
    failure_id_id integer,
    issued_by character varying(550) NOT NULL,
    l1_date date,
    l1_time time without time zone,
    signature_img text,
    l2_date date,
    l2_time time without time zone,
    received_by character varying(550) NOT NULL,
    signature_img2 text,
    follow_up_details text,
    handed_over character varying(550) NOT NULL,
    new_supervisor character varying(550) NOT NULL,
    signature_img3 text,
    completion_date date,
    completion_date_time time without time zone,
    completion_name character varying(550) NOT NULL,
    down_time character varying(550) NOT NULL,
    signature_img4 text,
    train_can_be_energized character varying(550) NOT NULL,
    train_can_be_moved character varying(550) NOT NULL,
    completion_date2 date,
    completion_date_time2 time without time zone,
    completion_name2 character varying(550) NOT NULL,
    corrective_action text,
    down_time2 character varying(550) NOT NULL,
    sic_has_performed character varying(550) NOT NULL,
    sic_start_time character varying(550) NOT NULL,
    signature_img5 text,
    train_can_be_energized2 character varying(550) NOT NULL,
    train_can_be_moved2 character varying(550) NOT NULL,
    details_of_the_activitues text,
    close_date date,
    close_name character varying(550) NOT NULL,
    close_time time without time zone,
    signature_img6 text
);


ALTER TABLE public.fracas_jobcard OWNER TO postgres;

--
-- Name: fracas_jobcard_job_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_jobcard_job_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_jobcard_job_id_seq OWNER TO postgres;

--
-- Name: fracas_jobcard_job_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_jobcard_job_id_seq OWNED BY public.fracas_jobcard.job_id;


--
-- Name: fracas_jobcardids; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_jobcardids (
    uid_id integer NOT NULL,
    year character varying(550),
    month character varying(550),
    last_id integer NOT NULL
);


ALTER TABLE public.fracas_jobcardids OWNER TO postgres;

--
-- Name: fracas_jobcardids_uid_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_jobcardids_uid_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_jobcardids_uid_id_seq OWNER TO postgres;

--
-- Name: fracas_jobcardids_uid_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_jobcardids_uid_id_seq OWNED BY public.fracas_jobcardids.uid_id;


--
-- Name: fracas_jobdetails; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_jobdetails (
    job_details_id integer NOT NULL,
    s_no character varying(550),
    job_description text,
    is_active integer NOT NULL,
    job_card_id_id integer
);


ALTER TABLE public.fracas_jobdetails OWNER TO postgres;

--
-- Name: fracas_jobdetails_job_details_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_jobdetails_job_details_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_jobdetails_job_details_id_seq OWNER TO postgres;

--
-- Name: fracas_jobdetails_job_details_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_jobdetails_job_details_id_seq OWNED BY public.fracas_jobdetails.job_details_id;


--
-- Name: fracas_jobreplacedequipment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_jobreplacedequipment (
    job_equipment_id integer NOT NULL,
    jobequipment_name character varying(550),
    jobequipment_new_no character varying(550),
    jobequipment_old_no character varying(550),
    is_active integer NOT NULL,
    job_card_id_id integer
);


ALTER TABLE public.fracas_jobreplacedequipment OWNER TO postgres;

--
-- Name: fracas_jobreplacedequipment_job_equipment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_jobreplacedequipment_job_equipment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_jobreplacedequipment_job_equipment_id_seq OWNER TO postgres;

--
-- Name: fracas_jobreplacedequipment_job_equipment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_jobreplacedequipment_job_equipment_id_seq OWNED BY public.fracas_jobreplacedequipment.job_equipment_id;


--
-- Name: fracas_jobworktomaintainers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_jobworktomaintainers (
    job_work_id integer NOT NULL,
    jobwork_name character varying(550),
    jobwork_work text,
    jobwork_signature text,
    is_active integer NOT NULL,
    job_card_id_id integer
);


ALTER TABLE public.fracas_jobworktomaintainers OWNER TO postgres;

--
-- Name: fracas_jobworktomaintainers_job_work_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_jobworktomaintainers_job_work_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_jobworktomaintainers_job_work_id_seq OWNER TO postgres;

--
-- Name: fracas_jobworktomaintainers_job_work_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_jobworktomaintainers_job_work_id_seq OWNED BY public.fracas_jobworktomaintainers.job_work_id;


--
-- Name: fracas_kilometrereading; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_kilometrereading (
    km_id integer NOT NULL,
    date date,
    ts01_tkm character varying(550),
    ts02_tkm character varying(550),
    ts03_tkm character varying(550),
    ts04_tkm character varying(550),
    ts05_tkm character varying(550),
    ts06_tkm character varying(550),
    ts07_tkm character varying(550),
    ts08_tkm character varying(550),
    ts09_tkm character varying(550),
    ts10_tkm character varying(550),
    ts11_tkm character varying(550),
    ts12_tkm character varying(550),
    ts13_tkm character varying(550),
    ts14_tkm character varying(550),
    ts15_tkm character varying(550),
    ts16_tkm character varying(550),
    ts17_tkm character varying(550),
    ts18_tkm character varying(550),
    ts19_tkm character varying(550),
    ts20_tkm character varying(550),
    ts21_tkm character varying(550),
    ts22_tkm character varying(550),
    ts23_tkm character varying(550),
    ts24_tkm character varying(550),
    ts25_tkm character varying(550),
    ts26_tkm character varying(550),
    ts27_tkm character varying(550),
    ts28_tkm character varying(550),
    ts29_tkm character varying(550),
    ts30_tkm character varying(550),
    ts31_tkm character varying(550),
    ts32_tkm character varying(550),
    ts33_tkm character varying(550),
    ts34_tkm character varying(550)
);


ALTER TABLE public.fracas_kilometrereading OWNER TO postgres;

--
-- Name: fracas_kilometrereading_km_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_kilometrereading_km_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_kilometrereading_km_id_seq OWNER TO postgres;

--
-- Name: fracas_kilometrereading_km_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_kilometrereading_km_id_seq OWNED BY public.fracas_kilometrereading.km_id;


--
-- Name: fracas_ncrgeneration; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_ncrgeneration (
    rec_id integer NOT NULL,
    ncr_gen_id character varying(550),
    date text NOT NULL,
    "time" text NOT NULL,
    is_active integer NOT NULL,
    rootcause_id_id integer,
    action_date character varying(550),
    approved_date character varying(550),
    corrective_action_date character varying(550),
    defect_date character varying(550),
    fnl_date character varying(550),
    verification_date character varying(550),
    defect_time character varying(550),
    defect_description text,
    assembly_name text NOT NULL,
    assembly_no text NOT NULL,
    detection_workstation text NOT NULL,
    drawing_no text NOT NULL,
    green_red_channel text NOT NULL,
    inspector_name text NOT NULL,
    location_id text NOT NULL,
    sel_car text NOT NULL,
    serial_no text NOT NULL,
    "chkCritical" integer NOT NULL,
    "chkMajor" integer NOT NULL,
    "chkMinor" integer NOT NULL,
    defect_detected_by text NOT NULL,
    defect_detected_workstation text NOT NULL,
    defect_location text NOT NULL,
    defect_source text NOT NULL,
    no_of_defective_parts text NOT NULL,
    no_of_parts_deloverd text NOT NULL,
    specification text NOT NULL,
    supplier_name text NOT NULL,
    active_deviations text NOT NULL,
    "chk_Internal" integer NOT NULL,
    "chk_Supplier" integer NOT NULL,
    "chk_TWL" integer NOT NULL,
    "chk_Transportation" integer NOT NULL,
    notok_img text,
    ok_img text,
    signature_img text,
    signature_img2 text,
    signature_img3 text,
    signature_img4 text,
    signature_img5 text,
    action_name text NOT NULL,
    approved_by text NOT NULL,
    approved_designation text NOT NULL,
    attachments_files character varying(550),
    containment_action text NOT NULL,
    corrective_action_by text NOT NULL,
    corrective_action_designation text NOT NULL,
    detection text NOT NULL,
    effectiveness text NOT NULL,
    initial_analysis text NOT NULL,
    inp_root_cause text NOT NULL,
    invoice_number text NOT NULL,
    non_conforming_part_disposition text NOT NULL,
    occurrence text NOT NULL,
    responsibility text NOT NULL,
    responsible_for_execution text NOT NULL,
    verification_name text NOT NULL,
    cost_1 character varying(550) NOT NULL,
    cost_2 character varying(550) NOT NULL,
    cost_3 character varying(550) NOT NULL,
    cost_4 character varying(550) NOT NULL,
    cost_5 character varying(550) NOT NULL,
    cost_6 character varying(550) NOT NULL,
    total_cost character varying(550) NOT NULL,
    fnl_designation text NOT NULL,
    fnl_name text NOT NULL,
    no_of_day_open text NOT NULL,
    physical_closure text NOT NULL,
    physical_closure_rca_capa text NOT NULL,
    asset_type character varying(550) NOT NULL,
    ncr_status integer NOT NULL,
    root_cause_analysis character varying(550) NOT NULL,
    rev_no character varying(550) NOT NULL,
    rejection_status integer NOT NULL,
    remark text NOT NULL,
    accept_status integer NOT NULL
);


ALTER TABLE public.fracas_ncrgeneration OWNER TO postgres;

--
-- Name: fracas_ncrgeneration_rec_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_ncrgeneration_rec_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_ncrgeneration_rec_id_seq OWNER TO postgres;

--
-- Name: fracas_ncrgeneration_rec_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_ncrgeneration_rec_id_seq OWNED BY public.fracas_ncrgeneration.rec_id;


--
-- Name: fracas_ncrids; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_ncrids (
    uid_id integer NOT NULL,
    year character varying(550),
    last_id integer NOT NULL
);


ALTER TABLE public.fracas_ncrids OWNER TO postgres;

--
-- Name: fracas_ncrids_uid_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_ncrids_uid_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_ncrids_uid_id_seq OWNER TO postgres;

--
-- Name: fracas_ncrids_uid_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_ncrids_uid_id_seq OWNED BY public.fracas_ncrids.uid_id;


--
-- Name: fracas_ncrimageslist; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_ncrimageslist (
    img_id integer NOT NULL,
    ncr_gen_id character varying(550),
    file_path text,
    is_active integer NOT NULL
);


ALTER TABLE public.fracas_ncrimageslist OWNER TO postgres;

--
-- Name: fracas_ncrimageslist_img_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_ncrimageslist_img_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_ncrimageslist_img_id_seq OWNER TO postgres;

--
-- Name: fracas_ncrimageslist_img_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_ncrimageslist_img_id_seq OWNED BY public.fracas_ncrimageslist.img_id;


--
-- Name: fracas_pbsmaster; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_pbsmaster (
    id integer NOT NULL,
    system character varying(550) NOT NULL,
    subsystem character varying(550) NOT NULL,
    product_id character varying(550) NOT NULL,
    product_description character varying(550) NOT NULL,
    asset_type character varying(550) NOT NULL,
    asset_description character varying(550) NOT NULL,
    "MTBF" double precision NOT NULL,
    "MTBSAF" double precision NOT NULL,
    "MART" double precision NOT NULL,
    asset_quantity integer NOT NULL,
    "MTTR" double precision NOT NULL,
    is_active integer NOT NULL,
    project_id integer,
    availability_target double precision NOT NULL
);


ALTER TABLE public.fracas_pbsmaster OWNER TO postgres;

--
-- Name: fracas_pbsmaster_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_pbsmaster_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_pbsmaster_id_seq OWNER TO postgres;

--
-- Name: fracas_pbsmaster_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_pbsmaster_id_seq OWNED BY public.fracas_pbsmaster.id;


--
-- Name: fracas_pbsunit; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_pbsunit (
    id integer NOT NULL,
    "MTBFMTBSAF" text NOT NULL,
    "MTTR" text NOT NULL,
    average_speed double precision NOT NULL,
    chk_average_speed double precision NOT NULL,
    num_of_days integer NOT NULL,
    running_time integer NOT NULL
);


ALTER TABLE public.fracas_pbsunit OWNER TO postgres;

--
-- Name: fracas_pbsunit_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_pbsunit_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_pbsunit_id_seq OWNER TO postgres;

--
-- Name: fracas_pbsunit_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_pbsunit_id_seq OWNED BY public.fracas_pbsunit.id;


--
-- Name: fracas_product; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_product (
    product_id integer NOT NULL,
    product_name character varying(50) NOT NULL,
    description character varying(100) NOT NULL,
    "MTBF" double precision NOT NULL,
    "MTBSAF" double precision NOT NULL,
    "MTTR" double precision NOT NULL,
    availability_target double precision NOT NULL,
    is_active integer NOT NULL,
    num_of_trains integer NOT NULL
);


ALTER TABLE public.fracas_product OWNER TO postgres;

--
-- Name: fracas_product_product_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_product_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_product_product_id_seq OWNER TO postgres;

--
-- Name: fracas_product_product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_product_product_id_seq OWNED BY public.fracas_product.product_id;


--
-- Name: fracas_reviewboard; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_reviewboard (
    id integer NOT NULL,
    asset_type character varying(550) NOT NULL,
    meeting_date date,
    meeting_id character varying(550),
    from_date date,
    to_date date,
    meeting_status character varying(550),
    meeting_outcome character varying(550),
    "P_id" integer NOT NULL,
    is_active integer NOT NULL
);


ALTER TABLE public.fracas_reviewboard OWNER TO postgres;

--
-- Name: fracas_reviewboard_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_reviewboard_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_reviewboard_id_seq OWNER TO postgres;

--
-- Name: fracas_reviewboard_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_reviewboard_id_seq OWNED BY public.fracas_reviewboard.id;


--
-- Name: fracas_rirgeneration_eir_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_rirgeneration_eir_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_rirgeneration_eir_id_seq OWNER TO postgres;

--
-- Name: fracas_rirgeneration_eir_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_rirgeneration_eir_id_seq OWNED BY public.fracas_eirgeneration.eir_id;


--
-- Name: fracas_rootcause; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_rootcause (
    root_cause_id integer NOT NULL,
    root_cause_description text NOT NULL,
    rca_workshop_date date,
    root_cause_status character varying(550) NOT NULL,
    defect_id integer,
    asset_type character varying(550) NOT NULL,
    immediate_cause text NOT NULL,
    leading_reasons text NOT NULL,
    "P_id" integer NOT NULL,
    is_active integer NOT NULL,
    material_is_damaged character varying(550) NOT NULL,
    organistaional_management_cause text NOT NULL,
    systemic_cause text NOT NULL,
    assembly_no text NOT NULL,
    failure_detection character varying(550) NOT NULL
);


ALTER TABLE public.fracas_rootcause OWNER TO postgres;

--
-- Name: fracas_rootcause_root_cause_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_rootcause_root_cause_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_rootcause_root_cause_id_seq OWNER TO postgres;

--
-- Name: fracas_rootcause_root_cause_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_rootcause_root_cause_id_seq OWNED BY public.fracas_rootcause.root_cause_id;


--
-- Name: fracas_systems; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_systems (
    id integer NOT NULL,
    "System" character varying(550) NOT NULL,
    "MTBF" double precision NOT NULL,
    "MTBSAF" double precision NOT NULL,
    "MTTR" double precision NOT NULL,
    availability_target double precision NOT NULL,
    is_active integer NOT NULL,
    project_id integer
);


ALTER TABLE public.fracas_systems OWNER TO postgres;

--
-- Name: fracas_systems_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_systems_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_systems_id_seq OWNER TO postgres;

--
-- Name: fracas_systems_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_systems_id_seq OWNED BY public.fracas_systems.id;


--
-- Name: fracas_temp_table_asset_register; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_temp_table_asset_register (
    id integer NOT NULL,
    asset_config_id character varying(550) NOT NULL,
    asset_serial_number character varying(550) NOT NULL,
    location_id text NOT NULL,
    location_description text NOT NULL,
    asset_type text NOT NULL,
    asset_type_id text NOT NULL,
    software_version character varying(550) NOT NULL,
    asset_description text NOT NULL,
    software_description text NOT NULL,
    asset_status character varying(550) NOT NULL,
    is_active integer NOT NULL,
    "P_id" text NOT NULL,
    error_list text NOT NULL,
    updated_by text NOT NULL
);


ALTER TABLE public.fracas_temp_table_asset_register OWNER TO postgres;

--
-- Name: fracas_temp_table_asset_register_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_temp_table_asset_register_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_temp_table_asset_register_id_seq OWNER TO postgres;

--
-- Name: fracas_temp_table_asset_register_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_temp_table_asset_register_id_seq OWNED BY public.fracas_temp_table_asset_register.id;


--
-- Name: fracas_temp_table_failure_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_temp_table_failure_data (
    id integer NOT NULL,
    failure_id bigint,
    asset_type text NOT NULL,
    asset_config_id text NOT NULL,
    asset_type_id text NOT NULL,
    event_description text NOT NULL,
    mode_id text NOT NULL,
    date text NOT NULL,
    "time" text NOT NULL,
    detection text NOT NULL,
    service_delay text NOT NULL,
    immediate_investigation text NOT NULL,
    failure_type text NOT NULL,
    safety_failure text NOT NULL,
    hazard_id text NOT NULL,
    cm_description text NOT NULL,
    replaced_asset_config_id text NOT NULL,
    cm_start_date text NOT NULL,
    cm_start_time text NOT NULL,
    cm_end_date text NOT NULL,
    cm_end_time text NOT NULL,
    oem_failure_reference text NOT NULL,
    defect text NOT NULL,
    error_list text NOT NULL,
    "P_id" text NOT NULL,
    updated_by text NOT NULL
);


ALTER TABLE public.fracas_temp_table_failure_data OWNER TO postgres;

--
-- Name: fracas_temp_table_failure_data_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_temp_table_failure_data_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_temp_table_failure_data_id_seq OWNER TO postgres;

--
-- Name: fracas_temp_table_failure_data_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_temp_table_failure_data_id_seq OWNED BY public.fracas_temp_table_failure_data.id;


--
-- Name: fracas_temp_table_failure_mode; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_temp_table_failure_mode (
    id integer NOT NULL,
    mode_id text NOT NULL,
    mode_description text NOT NULL,
    asset_type text NOT NULL,
    asset_type_id text NOT NULL,
    "P_id" text NOT NULL,
    updated_by text NOT NULL,
    error_list text NOT NULL
);


ALTER TABLE public.fracas_temp_table_failure_mode OWNER TO postgres;

--
-- Name: fracas_temp_table_failure_mode_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_temp_table_failure_mode_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_temp_table_failure_mode_id_seq OWNER TO postgres;

--
-- Name: fracas_temp_table_failure_mode_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_temp_table_failure_mode_id_seq OWNED BY public.fracas_temp_table_failure_mode.id;


--
-- Name: fracas_temp_table_failuredata; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_temp_table_failuredata (
    id integer NOT NULL,
    asset_type text NOT NULL,
    failure_id text NOT NULL,
    asset_config_id text NOT NULL,
    event_description text NOT NULL,
    mode_id text NOT NULL,
    mode_description text NOT NULL,
    date text NOT NULL,
    "time" text NOT NULL,
    detection text NOT NULL,
    service_delay text NOT NULL,
    immediate_investigation text NOT NULL,
    failure_type text NOT NULL,
    safety_failure text NOT NULL,
    hazard_id text NOT NULL,
    cm_description text NOT NULL,
    replaced_asset_config_id text NOT NULL,
    cm_start_date text NOT NULL,
    cm_start_time text NOT NULL,
    cm_end_date text NOT NULL,
    cm_end_time text NOT NULL,
    oem_failure_reference text NOT NULL,
    defect text NOT NULL,
    "P_id" text NOT NULL,
    is_active text NOT NULL,
    updated_by text NOT NULL
);


ALTER TABLE public.fracas_temp_table_failuredata OWNER TO postgres;

--
-- Name: fracas_temp_table_failuredata_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_temp_table_failuredata_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_temp_table_failuredata_id_seq OWNER TO postgres;

--
-- Name: fracas_temp_table_failuredata_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_temp_table_failuredata_id_seq OWNED BY public.fracas_temp_table_failuredata.id;


--
-- Name: fracas_temp_table_import_file; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_temp_table_import_file (
    id integer NOT NULL,
    system text NOT NULL,
    subsystem text NOT NULL,
    subsystem_id integer NOT NULL,
    product_id character varying(550) NOT NULL,
    product_description text NOT NULL,
    asset_type text NOT NULL,
    asset_description text NOT NULL,
    "MTBF" text NOT NULL,
    "MTBSAF" text NOT NULL,
    "MTTR" text NOT NULL,
    "MART" text NOT NULL,
    asset_quantity text NOT NULL,
    error_list text NOT NULL,
    updated_by text NOT NULL
);


ALTER TABLE public.fracas_temp_table_import_file OWNER TO postgres;

--
-- Name: fracas_temp_table_import_file_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_temp_table_import_file_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fracas_temp_table_import_file_id_seq OWNER TO postgres;

--
-- Name: fracas_temp_table_import_file_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fracas_temp_table_import_file_id_seq OWNED BY public.fracas_temp_table_import_file.id;


--
-- Name: fracas_userprofile_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_userprofile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2147483647
    CACHE 1;


ALTER TABLE public.fracas_userprofile_id_seq OWNER TO postgres;

--
-- Name: fracas_userprofile; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_userprofile (
    id integer DEFAULT nextval('public.fracas_userprofile_id_seq'::regclass) NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    product_id_id integer,
    user_role_id integer,
    is_active integer NOT NULL,
    is_disable integer NOT NULL
);


ALTER TABLE public.fracas_userprofile OWNER TO postgres;

--
-- Name: fracas_userresetkey_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fracas_userresetkey_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2147483647
    CACHE 1;


ALTER TABLE public.fracas_userresetkey_id_seq OWNER TO postgres;

--
-- Name: fracas_userresetkey; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fracas_userresetkey (
    id integer DEFAULT nextval('public.fracas_userresetkey_id_seq'::regclass) NOT NULL,
    key character varying(255) NOT NULL,
    expires_on timestamp with time zone,
    otp_expires_on timestamp with time zone,
    date timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.fracas_userresetkey OWNER TO postgres;

--
-- Name: admin_tools_stats_criteriatostatsm2m id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin_tools_stats_criteriatostatsm2m ALTER COLUMN id SET DEFAULT nextval('public.admin_tools_stats_criteriatostatsm2m_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: dash_stats_criteria id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dash_stats_criteria ALTER COLUMN id SET DEFAULT nextval('public.dash_stats_criteria_id_seq'::regclass);


--
-- Name: dashboard_stats id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_stats ALTER COLUMN id SET DEFAULT nextval('public.dashboard_stats_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: fracas_action action_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_action ALTER COLUMN action_id SET DEFAULT nextval('public.fracas_action_action_id_seq'::regclass);


--
-- Name: fracas_asset id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_asset ALTER COLUMN id SET DEFAULT nextval('public.fracas_asset_id_seq'::regclass);


--
-- Name: fracas_assetregister id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_assetregister ALTER COLUMN id SET DEFAULT nextval('public.fracas_assetregister_id_seq'::regclass);


--
-- Name: fracas_assetserialnumberids uid_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_assetserialnumberids ALTER COLUMN uid_id SET DEFAULT nextval('public.fracas_assetserialnumberids_uid_id_seq'::regclass);


--
-- Name: fracas_correctiveaction corrective_action_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_correctiveaction ALTER COLUMN corrective_action_id SET DEFAULT nextval('public.fracas_correctiveaction_corrective_action_id_seq'::regclass);


--
-- Name: fracas_defect defect_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_defect ALTER COLUMN defect_id SET DEFAULT nextval('public.fracas_defect_defect_id_seq'::regclass);


--
-- Name: fracas_defectdiscussion defect_discussion_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_defectdiscussion ALTER COLUMN defect_discussion_id SET DEFAULT nextval('public.fracas_defectdiscussion_defect_discussion_id_seq'::regclass);


--
-- Name: fracas_defectdiscussion_attendees id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_defectdiscussion_attendees ALTER COLUMN id SET DEFAULT nextval('public.fracas_defectdiscussion_attendees_id_seq'::regclass);


--
-- Name: fracas_eirgeneration eir_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_eirgeneration ALTER COLUMN eir_id SET DEFAULT nextval('public.fracas_rirgeneration_eir_id_seq'::regclass);


--
-- Name: fracas_eirids uid_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_eirids ALTER COLUMN uid_id SET DEFAULT nextval('public.fracas_eirids_uid_id_seq'::regclass);


--
-- Name: fracas_eirimages img_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_eirimages ALTER COLUMN img_id SET DEFAULT nextval('public.fracas_eirimages_img_id_seq'::regclass);


--
-- Name: fracas_employeemaster id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_employeemaster ALTER COLUMN id SET DEFAULT nextval('public.fracas_employeemaster_id_seq'::regclass);


--
-- Name: fracas_failuredata id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_failuredata ALTER COLUMN id SET DEFAULT nextval('public.fracas_failuredata_id_seq'::regclass);


--
-- Name: fracas_failuredataids uid_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_failuredataids ALTER COLUMN uid_id SET DEFAULT nextval('public.fracas_failuredataids_uid_id_seq'::regclass);


--
-- Name: fracas_failuremode id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_failuremode ALTER COLUMN id SET DEFAULT nextval('public.fracas_failuremode_id_seq'::regclass);


--
-- Name: fracas_history id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_history ALTER COLUMN id SET DEFAULT nextval('public.fracas_history_id_seq'::regclass);


--
-- Name: fracas_investigationdetails details_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_investigationdetails ALTER COLUMN details_id SET DEFAULT nextval('public.fracas_investigationdetails_details_id_seq'::regclass);


--
-- Name: fracas_jobcard job_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_jobcard ALTER COLUMN job_id SET DEFAULT nextval('public.fracas_jobcard_job_id_seq'::regclass);


--
-- Name: fracas_jobcardids uid_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_jobcardids ALTER COLUMN uid_id SET DEFAULT nextval('public.fracas_jobcardids_uid_id_seq'::regclass);


--
-- Name: fracas_jobdetails job_details_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_jobdetails ALTER COLUMN job_details_id SET DEFAULT nextval('public.fracas_jobdetails_job_details_id_seq'::regclass);


--
-- Name: fracas_jobreplacedequipment job_equipment_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_jobreplacedequipment ALTER COLUMN job_equipment_id SET DEFAULT nextval('public.fracas_jobreplacedequipment_job_equipment_id_seq'::regclass);


--
-- Name: fracas_jobworktomaintainers job_work_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_jobworktomaintainers ALTER COLUMN job_work_id SET DEFAULT nextval('public.fracas_jobworktomaintainers_job_work_id_seq'::regclass);


--
-- Name: fracas_kilometrereading km_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_kilometrereading ALTER COLUMN km_id SET DEFAULT nextval('public.fracas_kilometrereading_km_id_seq'::regclass);


--
-- Name: fracas_ncrgeneration rec_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_ncrgeneration ALTER COLUMN rec_id SET DEFAULT nextval('public.fracas_ncrgeneration_rec_id_seq'::regclass);


--
-- Name: fracas_ncrids uid_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_ncrids ALTER COLUMN uid_id SET DEFAULT nextval('public.fracas_ncrids_uid_id_seq'::regclass);


--
-- Name: fracas_ncrimageslist img_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_ncrimageslist ALTER COLUMN img_id SET DEFAULT nextval('public.fracas_ncrimageslist_img_id_seq'::regclass);


--
-- Name: fracas_pbsmaster id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_pbsmaster ALTER COLUMN id SET DEFAULT nextval('public.fracas_pbsmaster_id_seq'::regclass);


--
-- Name: fracas_pbsunit id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_pbsunit ALTER COLUMN id SET DEFAULT nextval('public.fracas_pbsunit_id_seq'::regclass);


--
-- Name: fracas_product product_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_product ALTER COLUMN product_id SET DEFAULT nextval('public.fracas_product_product_id_seq'::regclass);


--
-- Name: fracas_reviewboard id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_reviewboard ALTER COLUMN id SET DEFAULT nextval('public.fracas_reviewboard_id_seq'::regclass);


--
-- Name: fracas_rootcause root_cause_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_rootcause ALTER COLUMN root_cause_id SET DEFAULT nextval('public.fracas_rootcause_root_cause_id_seq'::regclass);


--
-- Name: fracas_systems id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_systems ALTER COLUMN id SET DEFAULT nextval('public.fracas_systems_id_seq'::regclass);


--
-- Name: fracas_temp_table_asset_register id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_temp_table_asset_register ALTER COLUMN id SET DEFAULT nextval('public.fracas_temp_table_asset_register_id_seq'::regclass);


--
-- Name: fracas_temp_table_failure_data id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_temp_table_failure_data ALTER COLUMN id SET DEFAULT nextval('public.fracas_temp_table_failure_data_id_seq'::regclass);


--
-- Name: fracas_temp_table_failure_mode id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_temp_table_failure_mode ALTER COLUMN id SET DEFAULT nextval('public.fracas_temp_table_failure_mode_id_seq'::regclass);


--
-- Name: fracas_temp_table_failuredata id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_temp_table_failuredata ALTER COLUMN id SET DEFAULT nextval('public.fracas_temp_table_failuredata_id_seq'::regclass);


--
-- Name: fracas_temp_table_import_file id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_temp_table_import_file ALTER COLUMN id SET DEFAULT nextval('public.fracas_temp_table_import_file_id_seq'::regclass);


--
-- Data for Name: admin_tools_stats_criteriatostatsm2m; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.admin_tools_stats_criteriatostatsm2m (id, "order", prefix, use_as, criteria_id, stats_id) FROM stdin;
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
1	Super Admin
2	Admin Level
4	view Level
5	Operator
6	Maintainer
3	FRACAS Engineer
7	Quality Team
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add dashboard stats	1	add_dashboardstats
2	Can change dashboard stats	1	change_dashboardstats
3	Can delete dashboard stats	1	delete_dashboardstats
4	Can view dashboard stats	1	view_dashboardstats
5	Can add dashboard stats criteria	2	add_dashboardstatscriteria
6	Can change dashboard stats criteria	2	change_dashboardstatscriteria
7	Can delete dashboard stats criteria	2	delete_dashboardstatscriteria
8	Can view dashboard stats criteria	2	view_dashboardstatscriteria
9	Can add criteria to stats m2m	3	add_criteriatostatsm2m
10	Can change criteria to stats m2m	3	change_criteriatostatsm2m
11	Can delete criteria to stats m2m	3	delete_criteriatostatsm2m
12	Can view criteria to stats m2m	3	view_criteriatostatsm2m
13	Can add log entry	4	add_logentry
14	Can change log entry	4	change_logentry
15	Can delete log entry	4	delete_logentry
16	Can view log entry	4	view_logentry
17	Can add permission	5	add_permission
18	Can change permission	5	change_permission
19	Can delete permission	5	delete_permission
20	Can view permission	5	view_permission
21	Can add group	6	add_group
22	Can change group	6	change_group
23	Can delete group	6	delete_group
24	Can view group	6	view_group
25	Can add user	7	add_user
26	Can change user	7	change_user
27	Can delete user	7	delete_user
28	Can view user	7	view_user
29	Can add content type	8	add_contenttype
30	Can change content type	8	change_contenttype
31	Can delete content type	8	delete_contenttype
32	Can view content type	8	view_contenttype
33	Can add session	9	add_session
34	Can change session	9	change_session
35	Can delete session	9	delete_session
36	Can view session	9	view_session
37	Can add asset	10	add_asset
38	Can change asset	10	change_asset
39	Can delete asset	10	delete_asset
40	Can view asset	10	view_asset
41	Can add defect	11	add_defect
42	Can change defect	11	change_defect
43	Can delete defect	11	delete_defect
44	Can view defect	11	view_defect
45	Can add failure mode	12	add_failuremode
46	Can change failure mode	12	change_failuremode
47	Can delete failure mode	12	delete_failuremode
48	Can view failure mode	12	view_failuremode
49	Can add failure data	13	add_failuredata
50	Can change failure data	13	change_failuredata
51	Can delete failure data	13	delete_failuredata
52	Can view failure data	13	view_failuredata
53	Can add corrective action	14	add_correctiveaction
54	Can change corrective action	14	change_correctiveaction
55	Can delete corrective action	14	delete_correctiveaction
56	Can view corrective action	14	view_correctiveaction
57	Can add root cause	15	add_rootcause
58	Can change root cause	15	change_rootcause
59	Can delete root cause	15	delete_rootcause
60	Can view root cause	15	view_rootcause
61	Can add review board	16	add_reviewboard
62	Can change review board	16	change_reviewboard
63	Can delete review board	16	delete_reviewboard
64	Can view review board	16	view_reviewboard
65	Can add defect discussion	17	add_defectdiscussion
66	Can change defect discussion	17	change_defectdiscussion
67	Can delete defect discussion	17	delete_defectdiscussion
68	Can view defect discussion	17	view_defectdiscussion
69	Can add action	18	add_action
70	Can change action	18	change_action
71	Can delete action	18	delete_action
72	Can view action	18	view_action
73	Can add employee master	19	add_employeemaster
74	Can change employee master	19	change_employeemaster
75	Can delete employee master	19	delete_employeemaster
76	Can view employee master	19	view_employeemaster
77	Can add pbs master	20	add_pbsmaster
78	Can change pbs master	20	change_pbsmaster
79	Can delete pbs master	20	delete_pbsmaster
80	Can view pbs master	20	view_pbsmaster
81	Can add user profile	21	add_userprofile
82	Can change user profile	21	change_userprofile
83	Can delete user profile	21	delete_userprofile
84	Can view user profile	21	view_userprofile
85	Can add user reset key	22	add_userresetkey
86	Can change user reset key	22	change_userresetkey
87	Can delete user reset key	22	delete_userresetkey
88	Can view user reset key	22	view_userresetkey
89	Can add asset register	23	add_assetregister
90	Can change asset register	23	change_assetregister
91	Can delete asset register	23	delete_assetregister
92	Can view asset register	23	view_assetregister
93	Can add product	24	add_product
94	Can change product	24	change_product
95	Can delete product	24	delete_product
96	Can view product	24	view_product
97	Can add temp failure data	25	add_tempfailuredata
98	Can change temp failure data	25	change_tempfailuredata
99	Can delete temp failure data	25	delete_tempfailuredata
100	Can view temp failure data	25	view_tempfailuredata
101	Can add temp_table_import_file	26	add_temp_table_import_file
102	Can change temp_table_import_file	26	change_temp_table_import_file
103	Can delete temp_table_import_file	26	delete_temp_table_import_file
104	Can view temp_table_import_file	26	view_temp_table_import_file
105	Can add temp_table_asset_register	27	add_temp_table_asset_register
106	Can change temp_table_asset_register	27	change_temp_table_asset_register
107	Can delete temp_table_asset_register	27	delete_temp_table_asset_register
108	Can view temp_table_asset_register	27	view_temp_table_asset_register
109	Can add temp_table_ failure data	28	add_temp_table_failuredata
110	Can change temp_table_ failure data	28	change_temp_table_failuredata
111	Can delete temp_table_ failure data	28	delete_temp_table_failuredata
112	Can view temp_table_ failure data	28	view_temp_table_failuredata
113	Can add temp_table_failure_mode	29	add_temp_table_failure_mode
114	Can change temp_table_failure_mode	29	change_temp_table_failure_mode
115	Can delete temp_table_failure_mode	29	delete_temp_table_failure_mode
116	Can view temp_table_failure_mode	29	view_temp_table_failure_mode
117	Can add temp_table_failure_data	30	add_temp_table_failure_data
118	Can change temp_table_failure_data	30	change_temp_table_failure_data
119	Can delete temp_table_failure_data	30	delete_temp_table_failure_data
120	Can view temp_table_failure_data	30	view_temp_table_failure_data
121	Can add history	31	add_history
122	Can change history	31	change_history
123	Can delete history	31	delete_history
124	Can view history	31	view_history
125	Can add pbs unit	32	add_pbsunit
126	Can change pbs unit	32	change_pbsunit
127	Can delete pbs unit	32	delete_pbsunit
128	Can view pbs unit	32	view_pbsunit
129	Can add systems	33	add_systems
130	Can change systems	33	change_systems
131	Can delete systems	33	delete_systems
132	Can view systems	33	view_systems
133	Can add job card i ds	34	add_jobcardids
134	Can change job card i ds	34	change_jobcardids
135	Can delete job card i ds	34	delete_jobcardids
136	Can view job card i ds	34	view_jobcardids
137	Can add job card	35	add_jobcard
138	Can change job card	35	change_jobcard
139	Can delete job card	35	delete_jobcard
140	Can view job card	35	view_jobcard
141	Can add job details	36	add_jobdetails
142	Can change job details	36	change_jobdetails
143	Can delete job details	36	delete_jobdetails
144	Can view job details	36	view_jobdetails
145	Can add job work to maintainers	37	add_jobworktomaintainers
146	Can change job work to maintainers	37	change_jobworktomaintainers
147	Can delete job work to maintainers	37	delete_jobworktomaintainers
148	Can view job work to maintainers	37	view_jobworktomaintainers
149	Can add job replaced equipment	38	add_jobreplacedequipment
150	Can change job replaced equipment	38	change_jobreplacedequipment
151	Can delete job replaced equipment	38	delete_jobreplacedequipment
152	Can view job replaced equipment	38	view_jobreplacedequipment
153	Can add failure data i ds	39	add_failuredataids
154	Can change failure data i ds	39	change_failuredataids
155	Can delete failure data i ds	39	delete_failuredataids
156	Can view failure data i ds	39	view_failuredataids
157	Can add eiri ds	40	add_eirids
158	Can change eiri ds	40	change_eirids
159	Can delete eiri ds	40	delete_eirids
160	Can view eiri ds	40	view_eirids
161	Can add eir generation	41	add_eirgeneration
162	Can change eir generation	41	change_eirgeneration
163	Can delete eir generation	41	delete_eirgeneration
164	Can view eir generation	41	view_eirgeneration
165	Can add investigation details	42	add_investigationdetails
166	Can change investigation details	42	change_investigationdetails
167	Can delete investigation details	42	delete_investigationdetails
168	Can view investigation details	42	view_investigationdetails
169	Can add eir images	43	add_eirimages
170	Can change eir images	43	change_eirimages
171	Can delete eir images	43	delete_eirimages
172	Can view eir images	43	view_eirimages
173	Can add kilometre reading	44	add_kilometrereading
174	Can change kilometre reading	44	change_kilometrereading
175	Can delete kilometre reading	44	delete_kilometrereading
176	Can view kilometre reading	44	view_kilometrereading
177	Can add ncri ds	45	add_ncrids
178	Can change ncri ds	45	change_ncrids
179	Can delete ncri ds	45	delete_ncrids
180	Can view ncri ds	45	view_ncrids
181	Can add ncr generation	46	add_ncrgeneration
182	Can change ncr generation	46	change_ncrgeneration
183	Can delete ncr generation	46	delete_ncrgeneration
184	Can view ncr generation	46	view_ncrgeneration
185	Can add asset serial number i ds	47	add_assetserialnumberids
186	Can change asset serial number i ds	47	change_assetserialnumberids
187	Can delete asset serial number i ds	47	delete_assetserialnumberids
188	Can view asset serial number i ds	47	view_assetserialnumberids
189	Can add ncr images list	48	add_ncrimageslist
190	Can change ncr images list	48	change_ncrimageslist
191	Can delete ncr images list	48	delete_ncrimageslist
192	Can view ncr images list	48	view_ncrimageslist
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, role) FROM stdin;
34	pbkdf2_sha256$216000$v4veIie6KYRq$okmag4L7syyhQHcdlsjGralA6gqFtv5l5QNe0xEkJXc=	\N	f	JohnSmith@gmail.com				f	t	2021-11-29 06:17:09.486324+00	0
30	pbkdf2_sha256$216000$KzOj913krwyr$vdcPtaavgB+/4IXJeTHyceAvq/tg1PN2pfvCSUGzuU4=	2021-11-29 07:27:18.920908+00	f	Tom@gmail.com				f	t	2021-11-29 06:15:17.255569+00	0
35	pbkdf2_sha256$180000$Z3vG4VSvSJwb$aknq3ADSrO5eE1NyEpcQON0I7cESJYD2sZWyR53aZr8=	2021-12-17 07:51:13.811675+00	t	sadmin@gmail.com				f	t	2021-12-17 07:41:50.021495+00	0
33	pbkdf2_sha256$180000$MNmYYOqevtEs$OwoZkdRD6xtof5bSUIQTVt+ptJYLmJ+zb4dMSvpOpJE=	2022-01-08 04:47:27.306825+00	f	JohnDoe@gmail.com				f	t	2021-11-29 06:16:36.35861+00	0
37	pbkdf2_sha256$216000$ISm04hkhdc5x$l675phFfMd022bYPMy71i6XfdF8a2pHKIv4FOhiipww=	2022-01-10 11:06:50.92132+00	f	intellex@rams				f	t	2022-01-10 04:38:32.99155+00	0
36	pbkdf2_sha256$216000$7n3P92uHkj4T$5jKYIWhIj62fDAI8e3559Z4oWKrsiswhtk5bmnZjY7g=	2022-01-11 03:59:02.56363+00	f	omkar@gmail.com				f	t	2022-01-08 07:05:38.511089+00	0
31	pbkdf2_sha256$180000$M8KTqAMhf7uf$jEMNdqis4KnjGH3Ncc5sl5d4+c8duKW8oh0qf6XMxGo=	2022-01-19 09:52:20.846346+00	f	Jerrry@gmail.com				f	t	2021-11-29 06:15:36.856597+00	0
38	pbkdf2_sha256$180000$cO924mJOkqjy$jFt6ZqXgTNEyCkfcMsf7o3hda1BY+MvUT/KxjYxz6hM=	2022-01-20 10:27:59.910428+00	f	sam@gmail.com				f	t	2022-01-19 10:08:18.39523+00	0
32	pbkdf2_sha256$180000$OwdsVdl7Mq26$dAQ8Af+QH7cte3+GeAkCaWRzyh8EfoMuj49hgSAVY4c=	2022-02-08 10:21:17.359326+00	f	Suhu@gmail.com				f	t	2021-11-29 06:16:00.263085+00	0
29	pbkdf2_sha256$216000$VYVkb2TRRxk3$XklhpLz7y4KxjqCkNNFhOMGbNSpiRgsr87C6tvTZDK0=	2022-02-18 06:43:18.34857+00	f	Gabriel@gmail.com				f	t	2021-11-29 06:14:48.700826+00	0
40	pbkdf2_sha256$180000$mBf8IzhZEZvE$no4v08TE+VWtF+q2wAzfz5uiHMzqNAKdIxq1VZtdgcA=	2025-08-02 11:16:34.216317+00	f	maintainer@gmail.com				f	t	2025-07-03 06:05:37.515034+00	0
39	pbkdf2_sha256$180000$t6KbravYFQWW$H4A2lqO5K9L9q+za61fomR1RYb9TV5WdaqGzwA95I80=	2025-08-01 09:36:34.95746+00	f	operator@gmail.com				f	t	2025-07-03 06:03:57.040154+00	0
49	pbkdf2_sha256$180000$zByghkVBz3if$8TNSW7xHD4GQ9rWMXEKTBgr/yy7MD8e8pk+EsmkeL68=	2025-08-03 09:45:11.767631+00	f	ramesh.bhukya@titagarh.in				f	t	2025-08-01 08:52:27.961991+00	0
46	pbkdf2_sha256$180000$KWGRrBNETyvY$KOBMPo3RTwIBc4TvYD+DrYMYsSY6BMdyzuHSNEPQoZU=	2025-08-01 08:46:55.40786+00	f	sandeep.jadhav@titagarh.in				f	t	2025-08-01 08:46:33.977661+00	0
42	pbkdf2_sha256$180000$LozpX37Fhurc$VOv3yfX4wJzQvVHoOaNgs/0CyFIwB9Wf6/9txMCn2o4=	\N	f	adminlevel@gmail.com				f	t	2025-07-03 06:09:41.512333+00	0
43	pbkdf2_sha256$180000$NwXDw9Da5WEE$GAHaEk8l98Hcss1gds2ORz39F5R2op+swE7/ythunTQ=	\N	f	viewlevel@gmail.com				f	t	2025-07-03 06:10:05.237049+00	0
41	pbkdf2_sha256$180000$DiHUXTJU030K$BVEvcHYT/qBEOiTzJWZj2/fIPV1PUXjaPaFgra1VU1w=	2025-07-29 10:03:52.904594+00	f	ram@gmail.com				f	t	2025-07-03 06:07:52.668599+00	0
47	pbkdf2_sha256$180000$ERTvtI4jTtu5$tTsCX1YAvCTf/0BqJADh8a6s1fxZ96cqL98DVBIe03g=	2025-08-01 08:48:42.752006+00	f	narayan.verma@titagarh.in				f	t	2025-08-01 08:48:24.200229+00	0
48	pbkdf2_sha256$180000$d5yGZ5f3NG4C$XhaL7Vz3Ptj41lvdS77mqOOC1N0dUWlR/jQezqpvXkw=	2025-08-01 08:50:49.939825+00	f	abhishek.verma@titagarh.in				f	t	2025-08-01 08:50:10.368067+00	0
28	pbkdf2_sha256$180000$KxLvyPvrTnxw$XE+7gdhW0rtgihgWV03lxueHH6wHDIzN/BW90fQOIvA=	2025-08-04 11:30:09.582358+00	t	admin@gmail.com				f	t	2021-11-29 04:52:54.692849+00	0
44	pbkdf2_sha256$180000$F1vMyIBmqbSs$xfg33ItY7uT1XhvFQNNmRT9qKNY4ARP1m81uSACa6F8=	2025-08-02 08:28:25.704407+00	f	rajkumaranumula@titagarh.in				f	t	2025-08-01 08:38:36.051881+00	0
50	pbkdf2_sha256$180000$rKk4B09lv4nj$RVoOyEY2sCQYgB08hzzxdayWg69LPBGCjweTTdJoM5g=	2025-08-02 08:32:53.300854+00	f	mahtab.alam@titagarh.in				f	t	2025-08-02 08:14:44.836033+00	0
45	pbkdf2_sha256$180000$0nTYUWD8rHuq$v0p1yedGp+k6FiRr2wOu88kDASoqVW81ApBaZyCCw9o=	2025-08-02 08:36:40.201597+00	f	mahendra.jadaun@titagarh.in				f	t	2025-08-01 08:43:51.560441+00	0
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: dash_stats_criteria; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dash_stats_criteria (id, criteria_name, criteria_fix_mapping, dynamic_criteria_field_name, criteria_dynamic_mapping, created_date, updated_date) FROM stdin;
\.


--
-- Data for Name: dashboard_stats; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_stats (id, graph_key, graph_title, model_app_name, model_name, date_field_name, operation_field_name, type_operation_field_name, is_visible, created_date, updated_date, user_field_name, default_chart_type, default_time_period, default_time_scale, y_axis_format, "distinct") FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin_tools_stats	dashboardstats
2	admin_tools_stats	dashboardstatscriteria
3	admin_tools_stats	criteriatostatsm2m
4	admin	logentry
5	auth	permission
6	auth	group
7	auth	user
8	contenttypes	contenttype
9	sessions	session
10	fracas	asset
11	fracas	defect
12	fracas	failuremode
13	fracas	failuredata
14	fracas	correctiveaction
15	fracas	rootcause
16	fracas	reviewboard
17	fracas	defectdiscussion
18	fracas	action
19	fracas	employeemaster
20	fracas	pbsmaster
21	fracas	userprofile
22	fracas	userresetkey
23	fracas	assetregister
24	fracas	product
25	fracas	tempfailuredata
26	fracas	temp_table_import_file
27	fracas	temp_table_asset_register
28	fracas	temp_table_failuredata
29	fracas	temp_table_failure_mode
30	fracas	temp_table_failure_data
31	fracas	history
32	fracas	pbsunit
33	fracas	systems
34	fracas	jobcardids
35	fracas	jobcard
36	fracas	jobdetails
37	fracas	jobworktomaintainers
38	fracas	jobreplacedequipment
39	fracas	failuredataids
40	fracas	eirids
41	fracas	eirgeneration
42	fracas	investigationdetails
43	fracas	eirimages
44	fracas	kilometrereading
45	fracas	ncrids
46	fracas	ncrgeneration
47	fracas	assetserialnumberids
48	fracas	ncrimageslist
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
49	contenttypes	0001_initial	2021-04-28 16:05:14.312237+00
50	auth	0001_initial	2021-04-28 16:05:14.330623+00
51	admin	0001_initial	2021-04-28 16:05:14.340066+00
52	admin	0002_logentry_remove_auto_add	2021-04-28 16:05:14.36114+00
53	admin	0003_logentry_add_action_flag_choices	2021-04-28 16:05:14.379112+00
54	admin_tools_stats	0001_initial	2021-04-28 16:05:14.385188+00
55	admin_tools_stats	0002_auto_20190920_1058	2021-04-28 16:05:14.396035+00
56	admin_tools_stats	0003_auto_20191007_0950	2021-04-28 16:05:14.41084+00
57	admin_tools_stats	0004_dashboardstats_y_tick_format	2021-04-28 16:05:14.418659+00
58	admin_tools_stats	0005_auto_20200203_1537	2021-04-28 16:05:14.426758+00
59	admin_tools_stats	0006_auto_20200205_0944	2021-04-28 16:05:14.43873+00
60	admin_tools_stats	0007_auto_20200205_1054	2021-04-28 16:05:14.446613+00
61	contenttypes	0002_remove_content_type_name	2021-04-28 16:05:14.456925+00
62	auth	0002_alter_permission_name_max_length	2021-04-28 16:05:14.470672+00
63	auth	0003_alter_user_email_max_length	2021-04-28 16:05:14.478636+00
64	auth	0004_alter_user_username_opts	2021-04-28 16:05:14.488993+00
65	auth	0005_alter_user_last_login_null	2021-04-28 16:05:14.498664+00
66	auth	0006_require_contenttypes_0002	2021-04-28 16:05:14.506626+00
67	auth	0007_alter_validators_add_error_messages	2021-04-28 16:05:14.522665+00
68	auth	0008_alter_user_username_max_length	2021-04-28 16:05:14.531078+00
69	auth	0009_alter_user_last_name_max_length	2021-04-28 16:05:14.548918+00
70	auth	0010_alter_group_name_max_length	2021-04-28 16:05:14.561745+00
71	auth	0011_update_proxy_permissions	2021-04-28 16:05:14.578694+00
72	fracas	0001_initial	2021-04-28 16:05:14.585099+00
73	sessions	0001_initial	2021-04-28 16:05:14.618754+00
74	fracas	0002_auto_20210428_1642	2021-04-29 03:42:14.072359+00
75	fracas	0003_auto_20210429_0317	2021-04-29 03:42:15.433626+00
76	fracas	0004_failuredata_asset_type	2021-05-13 17:07:12.228878+00
77	fracas	0002_auto_20211109_1445	2021-11-09 09:15:53.565526+00
78	fracas	0003_auto_20211109_1455	2021-11-09 09:25:25.005216+00
79	fracas	0004_auto_20211109_2005	2021-11-09 14:35:37.584761+00
80	fracas	0005_auto_20211111_1320	2021-11-11 07:50:31.14061+00
81	fracas	0006_auto_20211111_1527	2021-11-11 09:58:06.45078+00
82	fracas	0007_pbsmaster_is_active	2021-11-12 07:18:45.452223+00
83	fracas	0008_auto_20211112_1405	2021-11-12 08:36:18.637621+00
84	fracas	0009_asset_p_id	2021-11-13 05:31:41.954573+00
85	fracas	0010_auto_20211115_1115	2021-11-15 05:45:36.903036+00
86	fracas	0011_auto_20211115_1603	2021-11-15 10:33:45.885596+00
87	fracas	0012_tempfailuredata	2021-11-16 08:29:06.594882+00
88	fracas	0013_auto_20211116_1747	2021-11-16 12:17:31.402188+00
89	fracas	0014_auto_20211118_1128	2021-11-18 05:59:06.123894+00
90	fracas	0015_delete_tempfailuredata	2021-11-18 06:11:08.977541+00
91	fracas	0016_auto_20211119_1321	2021-11-19 07:51:32.497215+00
92	fracas	0017_auto_20211119_1742	2021-11-19 12:12:13.065973+00
93	fracas	0018_auto_20211120_1450	2021-11-20 09:20:50.59738+00
94	fracas	0019_auto_20211122_1208	2021-11-22 09:26:34.517078+00
95	fracas	0020_auto_20211122_1215	2021-11-22 09:26:34.581067+00
96	fracas	0021_auto_20211122_1231	2021-11-22 09:26:34.661058+00
97	fracas	0022_auto_20211122_1317	2021-11-22 09:26:34.789039+00
98	fracas	0023_auto_20211122_1322	2021-11-22 09:26:34.900048+00
99	fracas	0024_defectdiscussion1	2021-11-22 09:26:35.028029+00
100	fracas	0025_auto_20211122_1328	2021-11-22 09:39:53.352512+00
101	fracas	0026_auto_20211122_1331	2021-11-22 09:39:53.585544+00
102	fracas	0027_auto_20211122_1334	2021-11-22 09:39:53.665533+00
103	fracas	0028_auto_20211122_1337	2021-11-22 09:39:53.729524+00
104	fracas	0029_defectdiscussion_sample	2021-11-22 09:39:53.761527+00
105	fracas	0030_auto_20211122_1435	2021-11-22 09:39:53.858902+00
106	fracas	0031_auto_20211122_1440	2021-11-22 09:39:53.898905+00
107	fracas	0032_defectdiscussion_description	2021-11-22 09:39:53.914904+00
108	fracas	0033_employeemaster_description	2021-11-22 09:39:53.9309+00
109	fracas	0034_remove_employeemaster_description	2021-11-22 09:39:53.938899+00
110	fracas	0035_auto_20211122_1511	2021-11-22 09:42:09.023455+00
111	auth	0012_alter_user_first_name_max_length	2021-12-07 07:25:08.733453+00
112	fracas	0036_temp_table_import_file	2021-12-07 07:25:08.895868+00
113	fracas_admin	0001_initial	2021-12-07 07:25:09.001434+00
114	fracas_admin	0002_delete_temp_table_import_file	2021-12-07 07:25:09.018092+00
115	fracas	0037_auto_20211207_1450	2021-12-07 09:20:35.610398+00
116	fracas	0038_temp_table_asset_register	2021-12-17 06:27:37.611999+00
117	fracas	0039_auto_20211209_1346	2021-12-17 06:27:37.853563+00
118	fracas	0040_temp_table_failuredata	2021-12-17 06:27:37.965342+00
119	fracas	0041_auto_20211209_1659	2021-12-17 06:27:38.255776+00
120	fracas	0042_temp_table_failuredata_updated_by	2021-12-17 06:27:38.298853+00
121	fracas	0043_auto_20211209_1750	2021-12-17 06:27:38.800378+00
122	fracas	0044_temp_table_failure_mode	2021-12-17 06:27:38.955283+00
123	fracas	0045_temp_table_failure_mode_error_list	2021-12-17 06:27:38.965276+00
124	fracas	0046_history_temp_table_failure_data	2021-12-17 06:27:39.169089+00
125	fracas	0047_auto_20211220_1543	2021-12-20 10:13:49.784351+00
126	fracas	0048_auto_20211220_1607	2021-12-20 10:37:11.952339+00
127	fracas	0049_auto_20211220_1635	2021-12-20 11:06:02.117487+00
128	fracas	0050_product_is_active	2021-12-21 09:55:28.816104+00
129	fracas	0051_pbsunit	2021-12-21 10:21:30.782469+00
130	fracas	0052_auto_20211221_1637	2021-12-21 11:07:11.718828+00
131	fracas	0053_auto_20220105_1238	2022-01-05 07:08:25.767155+00
132	fracas	0054_auto_20220105_1243	2022-01-05 07:14:02.802516+00
133	fracas	0055_auto_20220110_1340	2022-01-10 08:47:58.353731+00
134	fracas	0056_auto_20220110_1506	2022-01-10 09:36:17.17225+00
135	fracas	0057_auto_20220110_1517	2022-01-10 09:47:23.54805+00
136	fracas	0058_auto_20220110_1556	2022-01-10 10:26:44.07176+00
137	fracas	0059_auto_20220111_1018	2022-01-11 04:50:52.659511+00
138	fracas	0060_auto_20220112_1649	2022-01-14 05:39:39.875811+00
139	fracas	0061_auto_20220113_2101	2022-01-14 05:39:39.964048+00
140	fracas	0062_auto_20220113_2111	2022-01-14 05:39:39.975062+00
141	fracas	0063_auto_20220113_2113	2022-01-14 05:39:39.986054+00
142	fracas	0064_auto_20220113_2114	2022-01-14 05:39:39.998129+00
143	fracas	0065_auto_20220113_2115	2022-01-14 05:39:40.040789+00
144	fracas	0066_auto_20220117_1109	2022-01-19 07:35:23.821015+00
145	fracas	0067_auto_20220118_1355	2022-01-19 07:35:23.834586+00
146	fracas	0068_auto_20220119_1125	2022-01-19 07:35:23.905563+00
147	fracas	0069_auto_20220119_1424	2022-01-19 08:54:40.66123+00
148	fracas	0070_auto_20220121_0940	2022-01-25 12:12:18.766353+00
149	fracas	0071_history_function_name	2022-01-25 12:12:18.787416+00
150	fracas	0072_systems	2022-02-15 08:05:01.085036+00
151	fracas	0002_auto_20250305_1030	2025-03-05 05:00:31.81837+00
152	fracas	0003_product_num_of_trains	2025-03-21 05:11:50.297461+00
153	fracas	0073_auto_20250305_0616	2025-06-23 05:07:02.122566+00
154	fracas	0074_product_num_of_trains	2025-06-23 05:07:23.823127+00
155	fracas	0075_merge_20250616_0510	2025-06-23 05:07:23.833122+00
156	fracas	0076_auto_20250616_0516	2025-06-23 05:07:23.927748+00
157	fracas	0077_failuredata_incident	2025-06-23 05:07:23.939739+00
158	fracas	0078_failuredata_deboarding	2025-06-23 05:07:23.952733+00
159	fracas	0079_jobcardids	2025-06-23 05:07:24.149688+00
160	fracas	0080_jobcard	2025-06-23 05:07:24.273268+00
161	fracas	0081_jobcard_job_card_no	2025-06-23 05:07:24.279942+00
162	fracas	0082_jobcard_failure_id	2025-06-23 05:07:24.330907+00
163	fracas	0083_jobcard_run_status	2025-06-23 05:07:24.408046+00
164	fracas	0084_auto_20250617_0919	2025-06-23 05:07:24.471007+00
165	fracas	0085_jobdetails	2025-06-23 05:07:24.626245+00
166	fracas	0086_jobcard_sic_no	2025-06-23 05:07:24.693183+00
167	fracas	0087_auto_20250618_0940	2025-06-23 05:07:24.898635+00
168	fracas	0088_jobcard_jobdetails	2025-06-23 05:07:25.181984+00
169	fracas	0089_auto_20250618_1033	2025-06-23 05:07:25.281756+00
170	fracas	0090_auto_20250618_1131	2025-06-23 05:07:25.325802+00
171	fracas	0091_jobworktomaintainers	2025-06-23 05:07:25.497134+00
172	fracas	0092_auto_20250619_0632	2025-06-23 05:07:25.592467+00
173	fracas	0093_jobreplacedequipment	2025-06-23 05:07:25.715313+00
174	fracas	0094_auto_20250619_0924	2025-06-23 05:07:25.841091+00
175	fracas	0095_auto_20250619_1030	2025-06-23 05:07:25.940864+00
176	fracas	0096_jobcard_details_of_the_activitues	2025-06-23 05:07:25.953942+00
177	fracas	0097_auto_20250619_1126	2025-06-23 05:07:26.050877+00
178	fracas	0098_failuredataids	2025-06-25 07:53:34.401221+00
179	fracas	0099_eirids	2025-06-25 07:53:34.412683+00
180	fracas	0100_rirgeneration	2025-06-25 07:53:34.439827+00
181	fracas	0101_rirgeneration_eir_gen_id	2025-06-25 07:53:34.454003+00
182	fracas	0102_rename_rirgeneration_eirgeneration	2025-06-25 07:53:34.488003+00
183	fracas	0103_eirgeneration_component	2025-06-25 07:53:34.49703+00
184	fracas	0104_investigationdetails	2025-06-25 07:53:34.513172+00
185	fracas	0105_auto_20250624_1516	2025-06-25 07:53:34.641139+00
186	fracas	0106_eirimages	2025-06-25 07:53:34.659251+00
187	fracas	0107_auto_20250625_1126	2025-06-25 07:53:34.691816+00
188	fracas	0108_kilometrereading	2025-06-28 05:56:46.813808+00
189	fracas	0109_auto_20250702_1218	2025-07-09 11:35:45.751027+00
190	fracas	0110_ncrgeneration_ncrids	2025-07-09 11:35:45.798908+00
191	fracas	0111_auto_20250709_1201	2025-07-09 11:35:45.829647+00
192	fracas	0112_ncrgeneration_defect_time	2025-07-09 11:35:45.836549+00
193	fracas	0113_ncrgeneration_defect_description	2025-07-09 11:35:45.843241+00
194	fracas	0114_auto_20250709_1352	2025-07-09 11:35:45.978396+00
195	fracas	0115_auto_20250709_1409	2025-07-09 11:35:46.023288+00
196	fracas	0116_auto_20250709_1411	2025-07-09 11:35:46.065968+00
197	fracas	0117_auto_20250709_1422	2025-07-09 11:35:46.083672+00
198	fracas	0118_auto_20250709_1432	2025-07-09 11:35:46.128557+00
199	fracas	0119_auto_20250709_1509	2025-07-09 11:35:46.156242+00
200	fracas	0120_auto_20250709_1526	2025-07-09 11:35:46.196899+00
201	fracas	0121_auto_20250709_1536	2025-07-09 11:35:46.307872+00
202	fracas	0122_auto_20250709_1551	2025-07-09 11:35:46.363828+00
203	fracas	0123_auto_20250709_1607	2025-07-09 11:35:46.410479+00
204	fracas	0124_assetserialnumberids	2025-07-16 07:07:24.102539+00
205	fracas	0125_ncrgeneration_asset_type	2025-07-16 07:07:24.112149+00
206	fracas	0126_ncrgeneration_ncr_status	2025-07-17 06:17:03.078974+00
207	fracas	0127_ncrimageslist	2025-07-17 06:17:03.091197+00
208	fracas	0128_ncrgeneration_root_cause_analysis	2025-07-17 06:17:03.099748+00
209	fracas	0129_ncrgeneration_rev_no	2025-07-23 09:14:38.038279+00
210	fracas	0130_auto_20250801_1022	2025-08-01 05:40:04.079355+00
211	fracas	0131_rootcause_assembly_no	2025-08-02 07:09:33.955068+00
212	fracas	0132_ncrgeneration_rejection_status	2025-08-02 07:09:33.96423+00
213	fracas	0133_ncrgeneration_remark	2025-08-02 07:09:33.972507+00
214	fracas	0134_ncrgeneration_accept_status	2025-08-02 07:09:33.980284+00
215	fracas	0135_rootcause_failure_detection	2025-08-04 08:12:35.944713+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
yig0949fhiyl92ewbmn1dy9yfwvm91me	MTE2NzhkZWE2MDFlYjY4NzYzMTRmMzM4ZjUzYzQ1ZTdjNTM0NjJjNjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ODk4NDI1NjFjNzUwMGE0YTNkNWY4M2RiMjcyNThiMjU2NjVhNGNiIn0=	2020-05-18 18:33:51.793305+00
1uh9cive1nus8cvq28z5yyatwgulycij	ZTk2ZDM2NGQxMDk1MmNlYWFjM2EzYTgxNDA1MzE3N2UwMDk2Y2M3MTp7Il9hdXRoX3VzZXJfaWQiOiI1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiYjY4YTE4OWNlNjMxYzcwNmY2Y2JhNWQzYzA4ZmVkYWVlOTA4MmJlIn0=	2020-05-21 13:56:37.224581+00
b2x1ls3bg2ly87rvup5fsakoib7evxlz	ZTk2ZDM2NGQxMDk1MmNlYWFjM2EzYTgxNDA1MzE3N2UwMDk2Y2M3MTp7Il9hdXRoX3VzZXJfaWQiOiI1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiYjY4YTE4OWNlNjMxYzcwNmY2Y2JhNWQzYzA4ZmVkYWVlOTA4MmJlIn0=	2020-05-21 14:32:23.225272+00
uiul5e5x5hgyan1hkhxsfnxwpih57r3v	ZjZkYzc0YWY4YTBhYTYwNGM5ZWU0N2IxYTg3YWFlZmVjMzk4NjY5ZTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MGViYzRjNDVjOTkyNWIxZTc2NjgxNDMzZTc2MTllYjEwN2I4YTkwIn0=	2020-05-25 10:52:16.383816+00
efh8mea4egdyt5uqbeug4ey04aco9c1i	MDllMzJiYWY2MWVhNTE4ZjQxZGFmMzI4MGYxMGY5MzRlZGZjODA5MTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMzkzNGFjZjQ0ZmEyMzc3N2Y4M2ZjMjRmYzNiOGI0NzYzMWNmMjJkIn0=	2020-05-25 17:47:20.443417+00
eywqrpcggdxfoaevuvnfzyq8sv2xc0sg	ZTk2ZDM2NGQxMDk1MmNlYWFjM2EzYTgxNDA1MzE3N2UwMDk2Y2M3MTp7Il9hdXRoX3VzZXJfaWQiOiI1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiYjY4YTE4OWNlNjMxYzcwNmY2Y2JhNWQzYzA4ZmVkYWVlOTA4MmJlIn0=	2020-05-29 05:45:31.03393+00
gqg47lhobh30yarsg0kdhwdiepkbstug	MDllMzJiYWY2MWVhNTE4ZjQxZGFmMzI4MGYxMGY5MzRlZGZjODA5MTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMzkzNGFjZjQ0ZmEyMzc3N2Y4M2ZjMjRmYzNiOGI0NzYzMWNmMjJkIn0=	2020-06-08 06:18:21.255933+00
smp4yn9hkbdp4hktuumrtmco9se2f682	ZjZkYzc0YWY4YTBhYTYwNGM5ZWU0N2IxYTg3YWFlZmVjMzk4NjY5ZTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MGViYzRjNDVjOTkyNWIxZTc2NjgxNDMzZTc2MTllYjEwN2I4YTkwIn0=	2020-06-08 11:03:42.900141+00
ccpfjiiduejpkgihba73xq3yutlc5mvx	MDllMzJiYWY2MWVhNTE4ZjQxZGFmMzI4MGYxMGY5MzRlZGZjODA5MTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMzkzNGFjZjQ0ZmEyMzc3N2Y4M2ZjMjRmYzNiOGI0NzYzMWNmMjJkIn0=	2020-06-11 11:02:18.114101+00
dwvjxw5j0mpwslhfagzpp74gp9slmjt8	MDllMzJiYWY2MWVhNTE4ZjQxZGFmMzI4MGYxMGY5MzRlZGZjODA5MTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMzkzNGFjZjQ0ZmEyMzc3N2Y4M2ZjMjRmYzNiOGI0NzYzMWNmMjJkIn0=	2020-06-15 04:23:54.240259+00
xb4gb96kjpqhhhkctoydd8b30wj5cg7n	MDllMzJiYWY2MWVhNTE4ZjQxZGFmMzI4MGYxMGY5MzRlZGZjODA5MTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMzkzNGFjZjQ0ZmEyMzc3N2Y4M2ZjMjRmYzNiOGI0NzYzMWNmMjJkIn0=	2020-06-15 04:58:19.408749+00
j3d2zqzw586715yysobjgtym8w1w5f5s	MDllMzJiYWY2MWVhNTE4ZjQxZGFmMzI4MGYxMGY5MzRlZGZjODA5MTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMzkzNGFjZjQ0ZmEyMzc3N2Y4M2ZjMjRmYzNiOGI0NzYzMWNmMjJkIn0=	2020-06-18 09:24:03.259519+00
ki5rs8xo4o2qg2krcq34n2wsrtfnn20s	MDllMzJiYWY2MWVhNTE4ZjQxZGFmMzI4MGYxMGY5MzRlZGZjODA5MTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMzkzNGFjZjQ0ZmEyMzc3N2Y4M2ZjMjRmYzNiOGI0NzYzMWNmMjJkIn0=	2020-06-19 05:38:25.298876+00
5y7pxi216mqtrjfxukuk9b3i1optya3s	ZTk2ZDM2NGQxMDk1MmNlYWFjM2EzYTgxNDA1MzE3N2UwMDk2Y2M3MTp7Il9hdXRoX3VzZXJfaWQiOiI1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiYjY4YTE4OWNlNjMxYzcwNmY2Y2JhNWQzYzA4ZmVkYWVlOTA4MmJlIn0=	2020-06-20 08:18:21.743883+00
ih046tleh9jwoyh01epaymxv3v5tliog	MDllMzJiYWY2MWVhNTE4ZjQxZGFmMzI4MGYxMGY5MzRlZGZjODA5MTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMzkzNGFjZjQ0ZmEyMzc3N2Y4M2ZjMjRmYzNiOGI0NzYzMWNmMjJkIn0=	2020-07-03 14:32:56.763515+00
g7p6hh2mz7x40iws8cdsztdjluvdjimh	MDllMzJiYWY2MWVhNTE4ZjQxZGFmMzI4MGYxMGY5MzRlZGZjODA5MTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMzkzNGFjZjQ0ZmEyMzc3N2Y4M2ZjMjRmYzNiOGI0NzYzMWNmMjJkIn0=	2020-07-07 07:20:23.269687+00
9ld0y5ejzrpgd6pje0lkc3g8wn1lifu1	MDllMzJiYWY2MWVhNTE4ZjQxZGFmMzI4MGYxMGY5MzRlZGZjODA5MTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMzkzNGFjZjQ0ZmEyMzc3N2Y4M2ZjMjRmYzNiOGI0NzYzMWNmMjJkIn0=	2020-07-13 04:08:39.128046+00
8tz8uq3gzzzmbfgqkt69r8xvmlozel57	MDllMzJiYWY2MWVhNTE4ZjQxZGFmMzI4MGYxMGY5MzRlZGZjODA5MTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMzkzNGFjZjQ0ZmEyMzc3N2Y4M2ZjMjRmYzNiOGI0NzYzMWNmMjJkIn0=	2020-07-16 18:34:27.823202+00
hoaxm61mqj5aiofgxcmwybmk2dm2v19i	ZjZkYzc0YWY4YTBhYTYwNGM5ZWU0N2IxYTg3YWFlZmVjMzk4NjY5ZTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MGViYzRjNDVjOTkyNWIxZTc2NjgxNDMzZTc2MTllYjEwN2I4YTkwIn0=	2020-07-18 11:22:37.479156+00
dv0c3klr38s4zfzuf5bn4wynearr9emd	MDllMzJiYWY2MWVhNTE4ZjQxZGFmMzI4MGYxMGY5MzRlZGZjODA5MTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMzkzNGFjZjQ0ZmEyMzc3N2Y4M2ZjMjRmYzNiOGI0NzYzMWNmMjJkIn0=	2020-07-19 18:17:15.054562+00
h9ic6ykqq9bsapbcucdw6r0ystdeq1fw	Yzk0NWI1MjQ5NmI5NjEwNzdjNGVjODA2M2Q4Yjg3ZDc5ZThlOTUzNzp7Il9hdXRoX3VzZXJfaWQiOiI2IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxOWNlNDg4Yjk3NWEyN2VmMDllM2IxZGMwYzBkNGI0MDM4OTI4MmU3In0=	2020-07-22 09:34:32.979352+00
qq65e1786om22vabt5itccff9kua8rd5	MDllMzJiYWY2MWVhNTE4ZjQxZGFmMzI4MGYxMGY5MzRlZGZjODA5MTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMzkzNGFjZjQ0ZmEyMzc3N2Y4M2ZjMjRmYzNiOGI0NzYzMWNmMjJkIn0=	2020-07-23 07:40:20.768261+00
yucpiavz6ft9rb5kjbhf0znberjv2so8	MDllMzJiYWY2MWVhNTE4ZjQxZGFmMzI4MGYxMGY5MzRlZGZjODA5MTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMzkzNGFjZjQ0ZmEyMzc3N2Y4M2ZjMjRmYzNiOGI0NzYzMWNmMjJkIn0=	2020-07-30 07:44:16.898134+00
763j9mgzgpisjqpbuxg7rdnw745bpww1	MDllMzJiYWY2MWVhNTE4ZjQxZGFmMzI4MGYxMGY5MzRlZGZjODA5MTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMzkzNGFjZjQ0ZmEyMzc3N2Y4M2ZjMjRmYzNiOGI0NzYzMWNmMjJkIn0=	2020-08-08 14:12:36.890029+00
drm1z71jqs9ra4r5a4x2kvmu0dgnxdvt	MDllMzJiYWY2MWVhNTE4ZjQxZGFmMzI4MGYxMGY5MzRlZGZjODA5MTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMzkzNGFjZjQ0ZmEyMzc3N2Y4M2ZjMjRmYzNiOGI0NzYzMWNmMjJkIn0=	2020-08-10 13:46:15.197445+00
yw98b3csvxlb6qccb4fehah20t27l5e5	MDllMzJiYWY2MWVhNTE4ZjQxZGFmMzI4MGYxMGY5MzRlZGZjODA5MTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMzkzNGFjZjQ0ZmEyMzc3N2Y4M2ZjMjRmYzNiOGI0NzYzMWNmMjJkIn0=	2020-08-15 09:09:35.786551+00
cewynku3lmaw59bm31ur1sfqaciytdi7	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2020-09-12 06:07:39.170921+00
hsc2we9h5f40ghdop4cnstc4mq03u30g	NjMyZDRmMGFjYWIyYTk0YTc0ODI5ZDdiZWRlYzczMzFlNzQ4ZDgzYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MGViYzRjNDVjOTkyNWIxZTc2NjgxNDMzZTc2MTllYjEwN2I4YTkwIiwiZW1haWwiOiJwdXJ2YSIsImxvZ2luIjoidHJ1ZSJ9	2020-09-21 09:45:53.127535+00
v640sqlu5zs5klk4ks856v534uxezuxc	NzcyZjU3YTFiZGFiOTdlZjJjNDEzNTA5NzJkNTIwMjQ2NThmNGQzNzp7ImVtYWlsIjoicHVydmEiLCJsb2dpbiI6InRydWUiLCJfYXV0aF91c2VyX2lkIjoiNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTBlYmM0YzQ1Yzk5MjViMWU3NjY4MTQzM2U3NjE5ZWIxMDdiOGE5MCIsInJldmlld19ib2FyZF9pZCI6MTQsIl9tZXNzYWdlcyI6IltbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgZmFpbHVyZSBtb2RlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL2ZhaWx1cmVtb2RlLzI0OC9jaGFuZ2UvXFxcIj5aQy1GTS0xNDwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHJvb3QgY2F1c2UgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcm9vdGNhdXNlLzcvY2hhbmdlL1xcXCI+Um9vdENhdXNlIG9iamVjdCAoNyk8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl1dIn0=	2020-10-09 10:42:45.312198+00
m6j3bg86xhrysf2z1lr70tkpqsna3l4w	NTBlMTVkZjEyMjgxYjY3NzVjZTFiOTk3YWU5NWJmOThjOGY0NWY4Yjp7ImVtYWlsIjoibmlraGlsIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjE5Y2U0ODhiOTc1YTI3ZWYwOWUzYjFkYzBjMGQ0YjQwMzg5MjgyZTcifQ==	2020-10-12 16:39:32.786732+00
96ficmvgob9shliilcpyz445myltwghi	NGY2NzcwYzcxMWU0OWRjN2Y2ODkwZTFkMjg2OGU5ZWFhOWNmZTJmMzp7ImVtYWlsIjoicmlzaGlAaW50ZWxsZXh1ay5jb20iLCJfYXV0aF91c2VyX2lkIjoiMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMjM5MzRhY2Y0NGZhMjM3NzdmODNmYzI0ZmMzYjhiNDc2MzFjZjIyZCJ9	2020-09-10 13:12:23.524959+00
499nb7kjij829npvtpyob57ifg9p6fv0	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2020-10-17 08:53:07.098958+00
x5dq0qrqzrw5l17c4p3uow3hcd1jzpsr	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2020-12-04 06:56:43.385178+00
h8jkvqejdjk85yqx0w1vtzhn6nlina61	M2Q2NDg2ZDFkZmJmNDk1MjYzMzA3NjRhYzdmNjBhMDU5OWJmNDVlYTp7ImVtYWlsIjoicHVydmEiLCJsb2dpbiI6InRydWUiLCJfYXV0aF91c2VyX2lkIjoiNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTBlYmM0YzQ1Yzk5MjViMWU3NjY4MTQzM2U3NjE5ZWIxMDdiOGE5MCJ9	2020-12-04 06:59:59.515216+00
ph47jk92zg9ckf888vdwit6zrsbi7vvq	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2020-12-11 08:46:02.791705+00
rb4itnk2u4dco683ra26w40lenl6wo4y	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2020-12-11 09:06:05.228979+00
rfnlxzk91j0us3pjeoxw9owj64935c69	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2020-12-26 14:45:55.17081+00
h8vqb29l1r3ucf65qhp0yqw4zv3gfj0h	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2021-01-15 14:47:10.888669+00
rqteoysr2u3s7vko4kmb4pshp2i04s0d	NmYwNTQ3Y2M5MjlmNjg0YTkxMzk1M2Q1YThkYTY0ZWZjYzIwMjA2Njp7ImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoibWFqYTU3OTBAZ21haWwuY29tIiwiX2F1dGhfdXNlcl9pZCI6IjE1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4NDM4MWFiYjMzMDBhMzg4YzVlY2Y2MTZjOGRiODE0NmY0MjEyYjJjIn0=	2021-01-31 11:57:40.230421+00
dhvugc3d30bgznpdtikmthm5ybfvkvwg	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2021-02-03 06:08:21.599812+00
b27plp6a452v8bqlksjd7eqrhug8f4dj	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2021-02-04 10:39:01.841387+00
cupxnih1az2puzybfnbyx2qpk6cc9u1d	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2021-02-06 09:43:13.135234+00
dllqep26a1axol6rbpgll6zuh702w568	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2021-04-04 16:24:22.06194+00
x5lnryarn4rq38yx3am8pfz7w10cz5zq	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2021-04-07 18:16:26.468828+00
j38vawk7kvulz93gz0b7fnoocaf4j0h8	NzNiODE4M2EzNGRiNWFmY2U0OTVlMTc3NWQ2YjA4M2IxZDg0OTMwZjp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQiLCJfbWVzc2FnZXMiOiJbW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIGZhaWx1cmUgbW9kZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9mYWlsdXJlbW9kZS8yNTAvY2hhbmdlL1xcXCI+WkMtRk0tMDY8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIGZhaWx1cmUgbW9kZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9mYWlsdXJlbW9kZS8yNTAvY2hhbmdlL1xcXCI+WkMtRk0tMDY8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIGZhaWx1cmUgbW9kZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9mYWlsdXJlbW9kZS8yNTAvY2hhbmdlL1xcXCI+WkMtRk0tMDY8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSBkZWZlY3QgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvZGVmZWN0LzUxL2NoYW5nZS9cXFwiPjUxOiBQb29yIG5ldHdvcmsgY29ubmVjdGl2aXR5IGF0IHRoZSBsb2NhdGlvbjwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgZmFpbHVyZSBtb2RlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL2ZhaWx1cmVtb2RlLzI0OC9jaGFuZ2UvXFxcIj5aQy1GTS0xNDwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXV0iLCJyZXZpZXdfYm9hcmRfaWQiOjEyfQ==	2020-09-11 09:43:49.775046+00
hr15ssqz01tjmclis85gcvc5li5mkfux	NjcxZDRkYzkwMjA4ZWU2NjRkNTZmNGFhMzhiOTAyNjQ0Nzg4NjM3ZTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQiLCJfbWVzc2FnZXMiOiJbW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIGZhaWx1cmUgbW9kZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9mYWlsdXJlbW9kZS8xODgyL2NoYW5nZS9cXFwiPm1vZGUwMDY8L2E+XFx1MjAxZCB3YXMgYWRkZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSByb290IGNhdXNlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Jvb3RjYXVzZS8yNi9jaGFuZ2UvXFxcIj5Sb290Q2F1c2Ugb2JqZWN0ICgyNik8L2E+XFx1MjAxZCB3YXMgYWRkZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSByb290IGNhdXNlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Jvb3RjYXVzZS8yNi9jaGFuZ2UvXFxcIj5Sb290Q2F1c2Ugb2JqZWN0ICgyNik8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIGZhaWx1cmUgbW9kZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9mYWlsdXJlbW9kZS8xODgzL2NoYW5nZS9cXFwiPm1vZGUwMDA2PC9hPlxcdTIwMWQgd2FzIGFkZGVkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgcm9vdCBjYXVzZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9yb290Y2F1c2UvMzYvY2hhbmdlL1xcXCI+Um9vdENhdXNlIG9iamVjdCAoMzYpPC9hPlxcdTIwMWQgd2FzIGFkZGVkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgcm9vdCBjYXVzZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9yb290Y2F1c2UvMzYvY2hhbmdlL1xcXCI+Um9vdENhdXNlIG9iamVjdCAoMzYpPC9hPlxcdTIwMWQgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSByb290IGNhdXNlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Jvb3RjYXVzZS8zNi9jaGFuZ2UvXFxcIj5Sb290Q2F1c2Ugb2JqZWN0ICgzNik8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHJvb3QgY2F1c2UgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcm9vdGNhdXNlLzM2L2NoYW5nZS9cXFwiPlJvb3RDYXVzZSBvYmplY3QgKDM2KTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgcm9vdCBjYXVzZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9yb290Y2F1c2UvMzYvY2hhbmdlL1xcXCI+Um9vdENhdXNlIG9iamVjdCAoMzYpPC9hPlxcdTIwMWQgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSByb290IGNhdXNlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Jvb3RjYXVzZS8zOC9jaGFuZ2UvXFxcIj5Sb290Q2F1c2Ugb2JqZWN0ICgzOCk8L2E+XFx1MjAxZCB3YXMgYWRkZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSByb290IGNhdXNlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Jvb3RjYXVzZS8zNi9jaGFuZ2UvXFxcIj5Sb290Q2F1c2Ugb2JqZWN0ICgzNik8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwwLDI1LFwiU3VjY2Vzc2Z1bGx5IGRlbGV0ZWQgMiBSb290IENhdXNlIEFuYWx5c2lzLlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgZmFpbHVyZSBkYXRhIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL2ZhaWx1cmVkYXRhLzI3NTQ4L2NoYW5nZS9cXFwiPiA8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSBmYWlsdXJlIG1vZGUgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvZmFpbHVyZW1vZGUvMTg4NS9jaGFuZ2UvXFxcIj5URVNUTU9ERTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgZmFpbHVyZSBtb2RlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL2ZhaWx1cmVtb2RlLzE4ODUvY2hhbmdlL1xcXCI+VEVTVE1PREU8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIGZhaWx1cmUgbW9kZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9mYWlsdXJlbW9kZS8xODg1L2NoYW5nZS9cXFwiPlRFU1RNT0RFPC9hPlxcdTIwMWQgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSBmYWlsdXJlIG1vZGUgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvZmFpbHVyZW1vZGUvMTg3MC9jaGFuZ2UvXFxcIj5UVlMxNDwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXV0iLCJyZXZpZXdfYm9hcmRfaWQiOjM4fQ==	2021-06-09 04:48:45.206728+00
z13alujvnmijtzza1w2eh4ke939pw2vw	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2021-05-17 16:47:26.180023+00
r433li43fi6a9exex4rc1b96s9is6kb4	MGFkMDRhNGUzYTA2ZDdjNTJjMmY1MzIxMzNiOTM4M2RlYWUwYjgzNTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQiLCJyZXZpZXdfYm9hcmRfaWQiOjE1fQ==	2021-02-05 04:23:27.828239+00
a7oiioqajc3joti25b5yitduerfxwfxj	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2021-07-09 10:52:43.038473+00
bwk0kzi4vu46e1wstlubgyn5wxwd1nvo	Mzg5MDkxZTIyNzQ3ZWU4YzM3NTI5M2YwMDZhOWY3ZDA2ZDEwMTVhNTp7ImVtYWlsIjoibWFqYTU3OTBAZ21haWwuY29tIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjE1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4NDM4MWFiYjMzMDBhMzg4YzVlY2Y2MTZjOGRiODE0NmY0MjEyYjJjIiwiX21lc3NhZ2VzIjoiW1tcIl9fanNvbl9tZXNzYWdlXCIsMCwyNSxcIkltcG9ydCBmaW5pc2hlZCwgd2l0aCA1OSBuZXcgYW5kIDAgdXBkYXRlZCBmYWlsdXJlIEF0dHJpYnV0aW9uIEZvcm0uXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMCwyNSxcIkltcG9ydCBmaW5pc2hlZCwgd2l0aCA1OSBuZXcgYW5kIDAgdXBkYXRlZCBmYWlsdXJlIEF0dHJpYnV0aW9uIEZvcm0uXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMCwyNSxcIkltcG9ydCBmaW5pc2hlZCwgd2l0aCA2MSBuZXcgYW5kIDAgdXBkYXRlZCBmYWlsdXJlIEF0dHJpYnV0aW9uIEZvcm0uXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMCwyNSxcIkltcG9ydCBmaW5pc2hlZCwgd2l0aCA2MSBuZXcgYW5kIDAgdXBkYXRlZCBmYWlsdXJlIEF0dHJpYnV0aW9uIEZvcm0uXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSBmYWlsdXJlIGRhdGEgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvZmFpbHVyZWRhdGEvMjcyNTMvY2hhbmdlL1xcXCI+IDwvYT5cXHUyMDFkIHdhcyBhZGRlZCBzdWNjZXNzZnVsbHkuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSByb290IGNhdXNlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Jvb3RjYXVzZS8yNy9jaGFuZ2UvXFxcIj5Sb290Q2F1c2Ugb2JqZWN0ICgyNyk8L2E+XFx1MjAxZCB3YXMgYWRkZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSByb290IGNhdXNlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Jvb3RjYXVzZS8yOS9jaGFuZ2UvXFxcIj5Sb290Q2F1c2Ugb2JqZWN0ICgyOSk8L2E+XFx1MjAxZCB3YXMgYWRkZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSByb290IGNhdXNlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Jvb3RjYXVzZS8zMC9jaGFuZ2UvXFxcIj5Sb290Q2F1c2Ugb2JqZWN0ICgzMCk8L2E+XFx1MjAxZCB3YXMgYWRkZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSByb290IGNhdXNlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Jvb3RjYXVzZS8zMi9jaGFuZ2UvXFxcIj5Sb290Q2F1c2Ugb2JqZWN0ICgzMik8L2E+XFx1MjAxZCB3YXMgYWRkZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSByb290IGNhdXNlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Jvb3RjYXVzZS8zMi9jaGFuZ2UvXFxcIj5Sb290Q2F1c2Ugb2JqZWN0ICgzMik8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHJvb3QgY2F1c2UgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcm9vdGNhdXNlLzM1L2NoYW5nZS9cXFwiPlJvb3RDYXVzZSBvYmplY3QgKDM1KTwvYT5cXHUyMDFkIHdhcyBhZGRlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHJvb3QgY2F1c2UgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcm9vdGNhdXNlLzM1L2NoYW5nZS9cXFwiPlJvb3RDYXVzZSBvYmplY3QgKDM1KTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgZmFpbHVyZSBtb2RlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL2ZhaWx1cmVtb2RlLzE4ODQvY2hhbmdlL1xcXCI+TW9kZTkwMDA8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuXCJdXSJ9	2021-06-09 16:04:26.011446+00
bz5zk4xqwafi0t3url3k6rnis03sblxb	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2021-02-06 14:58:45.338925+00
4dpcr6bpmj0x212o6jwyq4lt1r78z0dp	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2021-06-11 13:07:32.967354+00
jk2v4cq8hcitvpcg7qm53h51e31ulkic	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2021-06-12 04:46:45.789139+00
v0eljq9c785qbe2ywyt8f6f5088qhtw4	MGU0OGQwOGYyYzMwNWQyMzFhMDA4YTBmNTg3MThhZDEyZWU5ZDJmNDp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQiLCJfbWVzc2FnZXMiOiJbW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHJvb3QgY2F1c2UgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcm9vdGNhdXNlLzE5L2NoYW5nZS9cXFwiPlJvb3RDYXVzZSBvYmplY3QgKDE5KTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgcm9vdCBjYXVzZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9yb290Y2F1c2UvMTgvY2hhbmdlL1xcXCI+Um9vdENhdXNlIG9iamVjdCAoMTgpPC9hPlxcdTIwMWQgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSByb290IGNhdXNlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Jvb3RjYXVzZS8xOC9jaGFuZ2UvXFxcIj5Sb290Q2F1c2Ugb2JqZWN0ICgxOCk8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgYWRkIGFub3RoZXIgcm9vdCBjYXVzZSBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHJvb3QgY2F1c2UgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcm9vdGNhdXNlLzIwL2NoYW5nZS9cXFwiPlJvb3RDYXVzZSBvYmplY3QgKDIwKTwvYT5cXHUyMDFkIHdhcyBhZGRlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHJvb3QgY2F1c2UgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcm9vdGNhdXNlLzIwL2NoYW5nZS9cXFwiPlJvb3RDYXVzZSBvYmplY3QgKDIwKTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgZmFpbHVyZSBtb2RlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL2ZhaWx1cmVtb2RlLzE4NzUvY2hhbmdlL1xcXCI+TU9ERTAwMTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgZmFpbHVyZSBtb2RlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL2ZhaWx1cmVtb2RlLzE4NzUvY2hhbmdlL1xcXCI+TU9ERTAwMTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgcm9vdCBjYXVzZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9yb290Y2F1c2UvMjIvY2hhbmdlL1xcXCI+Um9vdENhdXNlIG9iamVjdCAoMjIpPC9hPlxcdTIwMWQgd2FzIGFkZGVkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXV0iLCJyZXZpZXdfYm9hcmRfaWQiOjM2fQ==	2021-06-12 09:24:46.042875+00
lys9slxjn4e969227n0fsk8lkoxzla4q	ZjQyZmE1OGFhMDBjODVjZTA4ZDA1NzMxMzE1NTY1NzllNjIxNzE3Njp7ImVtYWlsIjoibWFqYTU3OTBAZ21haWwuY29tIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjE1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4NDM4MWFiYjMzMDBhMzg4YzVlY2Y2MTZjOGRiODE0NmY0MjEyYjJjIiwiX21lc3NhZ2VzIjoiW1tcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSBwYnMgbWFzdGVyIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Bic21hc3Rlci8yNzUvY2hhbmdlL1xcXCI+UEJTTWFzdGVyIG9iamVjdCAoMjc1KTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHBicyBtYXN0ZXIgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcGJzbWFzdGVyLzI3NS9jaGFuZ2UvXFxcIj5QQlNNYXN0ZXIgb2JqZWN0ICgyNzUpPC9hPlxcdTIwMWQgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgcGJzIG1hc3RlciBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9wYnNtYXN0ZXIvMjc1L2NoYW5nZS9cXFwiPlBCU01hc3RlciBvYmplY3QgKDI3NSk8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSBwYnMgbWFzdGVyIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Bic21hc3Rlci8yNzUvY2hhbmdlL1xcXCI+UEJTTWFzdGVyIG9iamVjdCAoMjc1KTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHBicyBtYXN0ZXIgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcGJzbWFzdGVyLzI3NS9jaGFuZ2UvXFxcIj5QQlNNYXN0ZXIgb2JqZWN0ICgyNzUpPC9hPlxcdTIwMWQgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LlwiXV0ifQ==	2021-07-13 07:47:37.001541+00
5tcppu000o6ikltn06z0xggjtd654j18	ZTNmZWNjNzExYzZiNzNjNWY4MWU0N2UzNTI1ZmIwOGE4NGJkYWJhNTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQiLCJfbWVzc2FnZXMiOiJbW1wiX19qc29uX21lc3NhZ2VcIiwwLDI1LFwiSW1wb3J0IGZpbmlzaGVkLCB3aXRoIDIgbmV3IGFuZCAwIHVwZGF0ZWQgUEJTIE1hc3Rlci5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwwLDI1LFwiU3VjY2Vzc2Z1bGx5IGRlbGV0ZWQgMiBQQlMgTWFzdGVyLlwiXV0ifQ==	2021-02-08 14:30:28.495362+00
jo28bshbwyxg5o00n6jm81fezlyhyalz	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2021-03-02 10:18:30.767824+00
q8bxvzji13sm57dpffc2lzyu76zv9l2q	MjA4ZGE2NWUxMDUwYjUwNTA0MjM5ZGQyM2JjODYxZmIxOGUyNDVmMTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQiLCJfbWVzc2FnZXMiOiJbW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHJvb3QgY2F1c2UgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcm9vdGNhdXNlLzE4L2NoYW5nZS9cXFwiPlJvb3RDYXVzZSBvYmplY3QgKDE4KTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgZmFpbHVyZSBtb2RlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL2ZhaWx1cmVtb2RlLzE4NzYvY2hhbmdlL1xcXCI+NTg5MzI1PC9hPlxcdTIwMWQgd2FzIGFkZGVkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgZmFpbHVyZSBtb2RlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL2ZhaWx1cmVtb2RlLzE4NzYvY2hhbmdlL1xcXCI+NTg5MzI1PC9hPlxcdTIwMWQgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSBmYWlsdXJlIG1vZGUgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvZmFpbHVyZW1vZGUvMTg3Ni9jaGFuZ2UvXFxcIj41ODkzMjU8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHJvb3QgY2F1c2UgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcm9vdGNhdXNlLzI1L2NoYW5nZS9cXFwiPlJvb3RDYXVzZSBvYmplY3QgKDI1KTwvYT5cXHUyMDFkIHdhcyBhZGRlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHJvb3QgY2F1c2UgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcm9vdGNhdXNlLzI1L2NoYW5nZS9cXFwiPlJvb3RDYXVzZSBvYmplY3QgKDI1KTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgcm9vdCBjYXVzZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9yb290Y2F1c2UvMzMvY2hhbmdlL1xcXCI+Um9vdENhdXNlIG9iamVjdCAoMzMpPC9hPlxcdTIwMWQgd2FzIGFkZGVkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgcm9vdCBjYXVzZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9yb290Y2F1c2UvMzcvY2hhbmdlL1xcXCI+Um9vdENhdXNlIG9iamVjdCAoMzcpPC9hPlxcdTIwMWQgd2FzIGFkZGVkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgcm9vdCBjYXVzZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9yb290Y2F1c2UvMzcvY2hhbmdlL1xcXCI+Um9vdENhdXNlIG9iamVjdCAoMzcpPC9hPlxcdTIwMWQgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSByb290IGNhdXNlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Jvb3RjYXVzZS8zNy9jaGFuZ2UvXFxcIj5Sb290Q2F1c2Ugb2JqZWN0ICgzNyk8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIGZhaWx1cmUgbW9kZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9mYWlsdXJlbW9kZS8xODc3L2NoYW5nZS9cXFwiPk1PREUwMDI8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIGZhaWx1cmUgZGF0YSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9mYWlsdXJlZGF0YS8yNzU0Ny9jaGFuZ2UvXFxcIj4gPC9hPlxcdTIwMWQgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSBmYWlsdXJlIGRhdGEgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvZmFpbHVyZWRhdGEvMjc1NDcvY2hhbmdlL1xcXCI+IDwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS5cIl1dIn0=	2021-06-11 12:37:41.643531+00
icupa3fzn3kywuvwflev1n5169fpc4u1	MTc2YWEyMjY1NGIzNzMwZDY0NWQ4Y2ZhZDE0OWFkNzhhZWMyNTBhZjp7ImVtYWlsIjoibWFqYTU3OTBAZ21haWwuY29tIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjE1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4NDM4MWFiYjMzMDBhMzg4YzVlY2Y2MTZjOGRiODE0NmY0MjEyYjJjIn0=	2021-02-23 06:19:01.630465+00
atwo0xdx0wf1oswc4rkxqkoqp62eiqig	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2021-03-02 10:00:40.04298+00
5pxdepkwiq06ecfu0j4nad3473bg12uv	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2021-03-06 05:33:04.948052+00
kqdyv2hgyhxt5kwxrqtfrwo3d3farv8d	YzU3ZTNlOWJiYTg3NTI0ZGI2YmI0MjNkYmQ3ODFjMWUyNTQ0MWU5ZDp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQiLCJfbWVzc2FnZXMiOiJbW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHJvb3QgY2F1c2UgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcm9vdGNhdXNlLzQxL2NoYW5nZS9cXFwiPlJvb3RDYXVzZSBvYmplY3QgKDQxKTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgcm9vdCBjYXVzZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9yb290Y2F1c2UvNDEvY2hhbmdlL1xcXCI+Um9vdENhdXNlIG9iamVjdCAoNDEpPC9hPlxcdTIwMWQgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGFkZCBhbm90aGVyIHJvb3QgY2F1c2UgYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSByb290IGNhdXNlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Jvb3RjYXVzZS8xNC9jaGFuZ2UvXFxcIj5Sb290Q2F1c2Ugb2JqZWN0ICgxNCk8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSByb290IGNhdXNlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Jvb3RjYXVzZS8zNi9jaGFuZ2UvXFxcIj5Sb290Q2F1c2Ugb2JqZWN0ICgzNik8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSByb290IGNhdXNlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Jvb3RjYXVzZS8xNC9jaGFuZ2UvXFxcIj5Sb290Q2F1c2Ugb2JqZWN0ICgxNCk8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMCwyNSxcIlN1Y2Nlc3NmdWxseSBkZWxldGVkIDEgcm9vdCBjYXVzZS5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHJvb3QgY2F1c2UgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcm9vdGNhdXNlLzM5L2NoYW5nZS9cXFwiPlJvb3RDYXVzZSBvYmplY3QgKDM5KTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgZmFpbHVyZSBtb2RlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL2ZhaWx1cmVtb2RlLzE4NjMvY2hhbmdlL1xcXCI+VFZTMDc8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSBmYWlsdXJlIG1vZGUgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvZmFpbHVyZW1vZGUvMTg1OS9jaGFuZ2UvXFxcIj5UVlMwMzwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIGZhaWx1cmUgbW9kZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9mYWlsdXJlbW9kZS8xODU5L2NoYW5nZS9cXFwiPlRWUzAzPC9hPlxcdTIwMWQgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgZmFpbHVyZSBtb2RlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL2ZhaWx1cmVtb2RlLzE4NTkvY2hhbmdlL1xcXCI+VFZTMDM8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSBmYWlsdXJlIG1vZGUgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvZmFpbHVyZW1vZGUvMTg1OS9jaGFuZ2UvXFxcIj5UVlMwMzwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIGZhaWx1cmUgbW9kZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9mYWlsdXJlbW9kZS8xODYwL2NoYW5nZS9cXFwiPlRWUzA0PC9hPlxcdTIwMWQgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgcGJzIG1hc3RlciBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9wYnNtYXN0ZXIvMjc1L2NoYW5nZS9cXFwiPlBCU01hc3RlciBvYmplY3QgKDI3NSk8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSBwYnMgbWFzdGVyIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Bic21hc3Rlci8yNzUvY2hhbmdlL1xcXCI+UEJTTWFzdGVyIG9iamVjdCAoMjc1KTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS5cIl1dIiwicmV2aWV3X2JvYXJkX2lkIjozOX0=	2021-06-16 06:41:45.635856+00
7e7d199sj5pnf414j1z92mz44qwf35rl	M2Q2NDg2ZDFkZmJmNDk1MjYzMzA3NjRhYzdmNjBhMDU5OWJmNDVlYTp7ImVtYWlsIjoicHVydmEiLCJsb2dpbiI6InRydWUiLCJfYXV0aF91c2VyX2lkIjoiNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTBlYmM0YzQ1Yzk5MjViMWU3NjY4MTQzM2U3NjE5ZWIxMDdiOGE5MCJ9	2021-03-08 08:30:06.355767+00
ygre25ajaif7j5ionxozry3zzf4xcaxp	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2021-03-13 06:21:25.383055+00
dahuh7fw5conoci9irm6n5sga0jb53i3	MTc2YWEyMjY1NGIzNzMwZDY0NWQ4Y2ZhZDE0OWFkNzhhZWMyNTBhZjp7ImVtYWlsIjoibWFqYTU3OTBAZ21haWwuY29tIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjE1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4NDM4MWFiYjMzMDBhMzg4YzVlY2Y2MTZjOGRiODE0NmY0MjEyYjJjIn0=	2021-03-25 15:10:47.028032+00
jr04kcd886amwqu0uvtmtpv7yy3d3ynw	ZGVlYTEzMjljMzBjMGNiNmMyYWFmMjc5MGQ1NWJjMWVhOWZkMzc2ZTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQiLCJyZXZpZXdfYm9hcmRfaWQiOjMzfQ==	2021-05-31 14:11:40.102672+00
ihntskha2flavy2r44t7w5rn0fs22ftt	M2Q2NDg2ZDFkZmJmNDk1MjYzMzA3NjRhYzdmNjBhMDU5OWJmNDVlYTp7ImVtYWlsIjoicHVydmEiLCJsb2dpbiI6InRydWUiLCJfYXV0aF91c2VyX2lkIjoiNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTBlYmM0YzQ1Yzk5MjViMWU3NjY4MTQzM2U3NjE5ZWIxMDdiOGE5MCJ9	2021-04-15 07:50:30.937239+00
q0iwjywxqth5r8rlrknbsjsu0w0q9mhv	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2021-04-16 10:08:51.344747+00
84a6138wrdolwrcu1um9u177lt1nm0m3	ZThlMDY1YTBjOGRkM2QxMzg2NzQyZTRjYmU3MWU0MmQ4OTA3N2NiZDp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQiLCJyZXZpZXdfYm9hcmRfaWQiOjE3fQ==	2021-04-17 08:03:19.917528+00
9fu1h7acz1wc5xzf85b7n23w83n4an3t	YzM3OTIyYTg5NTI5MDUwOGZkODZkNmVjYzQyNjVjMmQ4MjQyYjcwMzp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQiLCJfbWVzc2FnZXMiOiJbW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIGZhaWx1cmUgZGF0YSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9mYWlsdXJlZGF0YS8xNTYxOC9jaGFuZ2UvXFxcIj4gPC9hPlxcdTIwMWQgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgZmFpbHVyZSBkYXRhIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL2ZhaWx1cmVkYXRhLzE1NjE3L2NoYW5nZS9cXFwiPiA8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMCwyNSxcIkltcG9ydCBmaW5pc2hlZCwgd2l0aCA1OSBuZXcgYW5kIDAgdXBkYXRlZCBGYWlsdXJlIGRhdGEgQ29sbGVjdGlvbiBGb3JtLlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgZmFpbHVyZSBtb2RlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL2ZhaWx1cmVtb2RlLzE4NzUvY2hhbmdlL1xcXCI+MTg1MjU8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSBmYWlsdXJlIG1vZGUgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvZmFpbHVyZW1vZGUvMTg3NS9jaGFuZ2UvXFxcIj4xODUyNTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgZmFpbHVyZSBtb2RlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL2ZhaWx1cmVtb2RlLzE4NzUvY2hhbmdlL1xcXCI+MTg1MjU8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSBmYWlsdXJlIG1vZGUgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvZmFpbHVyZW1vZGUvMTg3NC9jaGFuZ2UvXFxcIj4xMzQ1NzwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgZmFpbHVyZSBtb2RlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL2ZhaWx1cmVtb2RlLzE4NzQvY2hhbmdlL1xcXCI+MTM0NTc8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSBmYWlsdXJlIG1vZGUgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvZmFpbHVyZW1vZGUvMTg3My9jaGFuZ2UvXFxcIj4xMTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgZmFpbHVyZSBtb2RlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL2ZhaWx1cmVtb2RlLzE4NzMvY2hhbmdlL1xcXCI+MTE8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSByb290IGNhdXNlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Jvb3RjYXVzZS8xNi9jaGFuZ2UvXFxcIj5Sb290Q2F1c2Ugb2JqZWN0ICgxNik8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHJvb3QgY2F1c2UgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcm9vdGNhdXNlLzE2L2NoYW5nZS9cXFwiPlJvb3RDYXVzZSBvYmplY3QgKDE2KTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgcm9vdCBjYXVzZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9yb290Y2F1c2UvMTYvY2hhbmdlL1xcXCI+Um9vdENhdXNlIG9iamVjdCAoMTYpPC9hPlxcdTIwMWQgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSByb290IGNhdXNlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Jvb3RjYXVzZS8xNi9jaGFuZ2UvXFxcIj5Sb290Q2F1c2Ugb2JqZWN0ICgxNik8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHJvb3QgY2F1c2UgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcm9vdGNhdXNlLzE2L2NoYW5nZS9cXFwiPlJvb3RDYXVzZSBvYmplY3QgKDE2KTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgcm9vdCBjYXVzZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9yb290Y2F1c2UvMTYvY2hhbmdlL1xcXCI+Um9vdENhdXNlIG9iamVjdCAoMTYpPC9hPlxcdTIwMWQgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSBmYWlsdXJlIGRhdGEgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvZmFpbHVyZWRhdGEvMjc0MzAvY2hhbmdlL1xcXCI+IDwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIGZhaWx1cmUgbW9kZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9mYWlsdXJlbW9kZS8xODc1L2NoYW5nZS9cXFwiPk1PREUwMDE8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIGZhaWx1cmUgbW9kZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9mYWlsdXJlbW9kZS8xODc1L2NoYW5nZS9cXFwiPk1PREUwMDE8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHJvb3QgY2F1c2UgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcm9vdGNhdXNlLzIxL2NoYW5nZS9cXFwiPlJvb3RDYXVzZSBvYmplY3QgKDIxKTwvYT5cXHUyMDFkIHdhcyBhZGRlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHJvb3QgY2F1c2UgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcm9vdGNhdXNlLzIxL2NoYW5nZS9cXFwiPlJvb3RDYXVzZSBvYmplY3QgKDIxKTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgcm9vdCBjYXVzZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9yb290Y2F1c2UvMjEvY2hhbmdlL1xcXCI+Um9vdENhdXNlIG9iamVjdCAoMjEpPC9hPlxcdTIwMWQgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSByb290IGNhdXNlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Jvb3RjYXVzZS8yMS9jaGFuZ2UvXFxcIj5Sb290Q2F1c2Ugb2JqZWN0ICgyMSk8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHJvb3QgY2F1c2UgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcm9vdGNhdXNlLzIxL2NoYW5nZS9cXFwiPlJvb3RDYXVzZSBvYmplY3QgKDIxKTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDAsMjUsXCJJbXBvcnQgZmluaXNoZWQsIHdpdGggNTkgbmV3IGFuZCAwIHVwZGF0ZWQgRmFpbHVyZSBkYXRhIENvbGxlY3Rpb24gRm9ybS5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIGZhaWx1cmUgbW9kZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9mYWlsdXJlbW9kZS8xODc2L2NoYW5nZS9cXFwiPjU4OTMyNTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgZmFpbHVyZSBtb2RlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL2ZhaWx1cmVtb2RlLzE4NzYvY2hhbmdlL1xcXCI+NTg5MzI1PC9hPlxcdTIwMWQgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSBmYWlsdXJlIG1vZGUgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvZmFpbHVyZW1vZGUvMTg3Ni9jaGFuZ2UvXFxcIj41ODkzMjU8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIGZhaWx1cmUgbW9kZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9mYWlsdXJlbW9kZS8xODc2L2NoYW5nZS9cXFwiPjU4OTMyNTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgZmFpbHVyZSBtb2RlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL2ZhaWx1cmVtb2RlLzE4NzcvY2hhbmdlL1xcXCI+TU9ERTAwMjwvYT5cXHUyMDFkIHdhcyBhZGRlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIGZhaWx1cmUgbW9kZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9mYWlsdXJlbW9kZS8xODc3L2NoYW5nZS9cXFwiPk1PREUwMDI8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIGZhaWx1cmUgbW9kZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9mYWlsdXJlbW9kZS8xODc3L2NoYW5nZS9cXFwiPk1PREUwMDI8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIGZhaWx1cmUgbW9kZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9mYWlsdXJlbW9kZS8xODc4L2NoYW5nZS9cXFwiPm1vZGUwMDM8L2E+XFx1MjAxZCB3YXMgYWRkZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSBmYWlsdXJlIG1vZGUgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvZmFpbHVyZW1vZGUvMTg3OS9jaGFuZ2UvXFxcIj5tb2RlMDA0PC9hPlxcdTIwMWQgd2FzIGFkZGVkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgZmFpbHVyZSBtb2RlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL2ZhaWx1cmVtb2RlLzE4NzkvY2hhbmdlL1xcXCI+bW9kZTAwNDwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgcm9vdCBjYXVzZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9yb290Y2F1c2UvMjMvY2hhbmdlL1xcXCI+Um9vdENhdXNlIG9iamVjdCAoMjMpPC9hPlxcdTIwMWQgd2FzIGFkZGVkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgcm9vdCBjYXVzZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9yb290Y2F1c2UvMjMvY2hhbmdlL1xcXCI+Um9vdENhdXNlIG9iamVjdCAoMjMpPC9hPlxcdTIwMWQgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSByb290IGNhdXNlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Jvb3RjYXVzZS8yMy9jaGFuZ2UvXFxcIj5Sb290Q2F1c2Ugb2JqZWN0ICgyMyk8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHJvb3QgY2F1c2UgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcm9vdGNhdXNlLzIzL2NoYW5nZS9cXFwiPlJvb3RDYXVzZSBvYmplY3QgKDIzKTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgcm9vdCBjYXVzZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9yb290Y2F1c2UvMjMvY2hhbmdlL1xcXCI+Um9vdENhdXNlIG9iamVjdCAoMjMpPC9hPlxcdTIwMWQgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSByb290IGNhdXNlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Jvb3RjYXVzZS8yMy9jaGFuZ2UvXFxcIj5Sb290Q2F1c2Ugb2JqZWN0ICgyMyk8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHJvb3QgY2F1c2UgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcm9vdGNhdXNlLzIzL2NoYW5nZS9cXFwiPlJvb3RDYXVzZSBvYmplY3QgKDIzKTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXSxbXCJfX2pzb25fbWVzc2FnZVwiLDEsMjUsXCJUaGUgcm9vdCBjYXVzZSBcXHUyMDFjPGEgaHJlZj1cXFwiL2FkbWluL2ZyYWNhcy9yb290Y2F1c2UvMjMvY2hhbmdlL1xcXCI+Um9vdENhdXNlIG9iamVjdCAoMjMpPC9hPlxcdTIwMWQgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LiBZb3UgbWF5IGVkaXQgaXQgYWdhaW4gYmVsb3cuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSByb290IGNhdXNlIFxcdTIwMWM8YSBocmVmPVxcXCIvYWRtaW4vZnJhY2FzL3Jvb3RjYXVzZS8yMy9jaGFuZ2UvXFxcIj5Sb290Q2F1c2Ugb2JqZWN0ICgyMyk8L2E+XFx1MjAxZCB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuIFlvdSBtYXkgZWRpdCBpdCBhZ2FpbiBiZWxvdy5cIl0sW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHJvb3QgY2F1c2UgXFx1MjAxYzxhIGhyZWY9XFxcIi9hZG1pbi9mcmFjYXMvcm9vdGNhdXNlLzIzL2NoYW5nZS9cXFwiPlJvb3RDYXVzZSBvYmplY3QgKDIzKTwvYT5cXHUyMDFkIHdhcyBjaGFuZ2VkIHN1Y2Nlc3NmdWxseS4gWW91IG1heSBlZGl0IGl0IGFnYWluIGJlbG93LlwiXV0iLCJyZXZpZXdfYm9hcmRfaWQiOjM3fQ==	2021-06-04 17:01:38.901601+00
nhqg2tcw6pl1usuy2jv1u28q9txcl3as	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2021-06-15 10:10:06.939948+00
2dl6ekdxfh6z9zif0s6fvgr9n9ioqq1c	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2021-04-19 15:01:04.811022+00
842xjzgdiwwruzdcecijspeao4a8aqal	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2021-04-27 07:57:12.788768+00
w2j89adospbra5a1d2dwpfufhh5yrum7	NWNlOTFmOTBjMTNkYTJiZmMzOTU1ZjBhNWEwMzhiNjBiNWY3ZTgzNjp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQiLCJyZXZpZXdfYm9hcmRfaWQiOjIwfQ==	2021-05-08 21:01:36.10996+00
2atmkvhcbfse0wx5o8xhg5k6lk310mhw	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2021-05-15 03:54:15.014584+00
4vvxeysk0xdddm9fnnz2cnlha3l8gqy6	MTVlNmNjZTlmNTcwNGIwYjdmMjVmYjNkOWVjNDUzYmYxY2E1ZWU2OTp7ImVtYWlsIjoiaW50ZWxsZXhyYW1zIiwibG9naW4iOiJ0cnVlIiwiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjIzOTM0YWNmNDRmYTIzNzc3ZjgzZmMyNGZjM2I4YjQ3NjMxY2YyMmQifQ==	2021-05-17 08:45:02.022669+00
kd2ordrd8p6xj5hr611tto9t4h78pkvi	NDc4MjQwYjc0NTcyMmEzOWYxMjM2NTFkODFhZWI2ZTczMGQ2ODZmMjp7Il9hdXRoX3VzZXJfaWQiOiIxNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNDAzZGM0M2ZiMjM4ZjVlYzhkMjc0YzAzZGQ0NTNmY2RmNGVhYzI3MyIsIlBfaWQiOjMsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiY2E5MDMzOTZAZ21haWwuY29tIiwidXNlcl9Sb2xlIjoyLCJ1c2VyX0lEIjoxNn0=	2021-12-03 09:12:35.607898+00
r1oer2lw6c4melwctriaksudbdh54siy	.eJxVjrsOgjAUht-lsyH0FGrLZIyLg4nxBcgpp0C1tAmXyfjuFsKg43_N92Y1LnNfL5Mda0esYgDs8GsabF42rAk9MXQxa2KYR2eytZLt6ZTdIll_3rt_Bz1OfVoLbttGlJqOhgTXSko0WkgCmRet4gJ5TsANWFKapOKlMsRV0WgQ0CqD6fS-EeYH5mPnQvqcx8Um3w7ofJJIgwunblWJckjJBvCI3rKK7-p6YRXA5wtPUE_B:1mqqbr:Q08ZrebjmV638Qp88yiK6mMQ6sDl_Ma0dBJwMWepNr8	2021-12-11 05:50:51.788325+00
wt2bnvhcm1h35hvz50g2umfl4fk7sg8s	ZmVkZTEwZWE2MTYxMjRkMDE5YTk4OTNlM2NjNTcxM2ZlODExYWRlNzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNGZmN2YzYmJkYWRlNjJmNzJiZGRkZGYxOTUzYzgzYTM0N2FlZDVmMyIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2021-12-21 08:08:03.459025+00
lm4qo8fp3ro43z2norc6oi22g1cuc49e	ZmVkZTEwZWE2MTYxMjRkMDE5YTk4OTNlM2NjNTcxM2ZlODExYWRlNzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNGZmN2YzYmJkYWRlNjJmNzJiZGRkZGYxOTUzYzgzYTM0N2FlZDVmMyIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2021-12-21 08:51:50.007894+00
6nyb02oq0ut7ssj4jms1v9k3nyyzhwe3	.eJxVjrsOgyAUht-F2RhEBHFqmi4dmjR9AXPggNIqJF6mpu9eNA7t-F_zvUkL69K362yn1iNpCKtJ9mtqMC8btgSfELqYmxiWyet8q-RHOue3iHY4H92_gx7mPq1dpShUWCgnqRMgKDeGIdfO8QrqUilW64IKDqglk2UpDGPIuCwrKxRqk07vOyHNyBA7H9LnMq02-XYEPyQJOPpw6jaVKMeU7ACPOFjSFIe6XkjD6s8XbOxP-w:1n2aLS:Hl7upqCp3Fe1q7b_wFUAbCMeiFwJ7aVS_bcxQ26BbQw	2022-01-12 14:54:26.289351+00
8b833ac5qf4knwq6rta8a9y9hejnzmr2	NGYxOGJhOWVlY2E5Y2E5YWNlYTQzYzFjYzA4NmI1NjhhMDRjYWE0Yzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMzdlYmM5ZDhkODVkNTlmYTZlZmRjZTBjNWQ2MzkzNGRkYmMyYmNmMiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2022-01-19 10:50:15.456518+00
021dqpubdh1fv04ser82g0l8nkriqtgw	NGYxOGJhOWVlY2E5Y2E5YWNlYTQzYzFjYzA4NmI1NjhhMDRjYWE0Yzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMzdlYmM5ZDhkODVkNTlmYTZlZmRjZTBjNWQ2MzkzNGRkYmMyYmNmMiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2022-01-20 11:04:39.546817+00
miv7spmitnr9qswwh4zasy3883mxrhyn	NGYxOGJhOWVlY2E5Y2E5YWNlYTQzYzFjYzA4NmI1NjhhMDRjYWE0Yzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMzdlYmM5ZDhkODVkNTlmYTZlZmRjZTBjNWQ2MzkzNGRkYmMyYmNmMiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2022-01-24 04:42:05.376015+00
3l43zbkkht5ranl0gc8l8bg6ap85qofi	NGYxOGJhOWVlY2E5Y2E5YWNlYTQzYzFjYzA4NmI1NjhhMDRjYWE0Yzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMzdlYmM5ZDhkODVkNTlmYTZlZmRjZTBjNWQ2MzkzNGRkYmMyYmNmMiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2022-01-24 08:27:23.135097+00
dgh4aj678tkxy03w8ivzn70obtrvzxy9	.eJxVTrsOgjAU_RdmJRTaYp3UuDiYEDVxJLf0FhBoEx6T8d-9EAbdzjvnHeQwjVU-DdjntQn2QSKDza-ooWjQzY55gSt9WHg39rUO50i4ukN49Qbb05r9G6hgqKidGh1zxhgoFWkTabQsFcpyDdIWseBGScOTHUfDWAIxKqWBRaSAQGEto9FseRjPwEGHNJqJ4_aRPe9ktr6sHUljPyFR7KBuifqugf5Qzoyed-Qsp26-pX6yssuZsPx8Ac5iVeA:1n78JK:88BjG6JCOMqzP4MjOWpnAdnKZsWrTM3UnyMod5tHHxg	2022-01-25 03:59:02.579636+00
fbz35ir48qjwzpc0uzwrwzryshxnz0gb	YjE1OWQ3OWZlMjU0YjE5OTllMmY0Yjk2NmJiZjYzNjQzY2MxZWFhMzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMGY0NDQ3NDNlNmI3M2IyOTlkZjY5MjY0NjUzYmFlZDlhYzFlYTI5ZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2022-01-25 09:44:06.161848+00
su9jmxm1vxttc6no8nxl9h2p5uhscsbh	YjI3NTIwMWZlYTU2N2EzOTQ4N2JlNjU4MmY5YzYwMjMzMmQwNjEwYTp7Il9hdXRoX3VzZXJfaWQiOiIyOSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNjk0YWUwNmRiMTA5ZGM3ZGE1NTkyNTNjZGRiMzg3MWVmYzFiN2VlNiIsIlBfaWQiOjEsIlBfbmFtZSI6IlA1LVNpZ25hbGxpbmciLCJsb2dpbiI6InRydWUiLCJlbWFpbCI6IkdhYnJpZWxAZ21haWwuY29tIiwidXNlcl9Sb2xlIjozLCJ1c2VyX0lEIjoyOX0=	2022-01-30 08:00:51.856261+00
tslcc68qx1e9jyz8gvgxducqlu5wv62z	YjE1OWQ3OWZlMjU0YjE5OTllMmY0Yjk2NmJiZjYzNjQzY2MxZWFhMzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMGY0NDQ3NDNlNmI3M2IyOTlkZjY5MjY0NjUzYmFlZDlhYzFlYTI5ZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2022-01-31 05:07:32.590427+00
nc3nnnge593e3yingp5vxtztevqryofb	YjE1OWQ3OWZlMjU0YjE5OTllMmY0Yjk2NmJiZjYzNjQzY2MxZWFhMzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMGY0NDQ3NDNlNmI3M2IyOTlkZjY5MjY0NjUzYmFlZDlhYzFlYTI5ZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2022-02-02 07:35:47.484285+00
8jemf2mwp49f2qx3immnrkf4lfgsgmkn	YjE1OWQ3OWZlMjU0YjE5OTllMmY0Yjk2NmJiZjYzNjQzY2MxZWFhMzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMGY0NDQ3NDNlNmI3M2IyOTlkZjY5MjY0NjUzYmFlZDlhYzFlYTI5ZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2022-02-02 09:48:11.600765+00
kyk9fa5uoszlk6ld8yndv36o0hdid5h8	YjI3NTIwMWZlYTU2N2EzOTQ4N2JlNjU4MmY5YzYwMjMzMmQwNjEwYTp7Il9hdXRoX3VzZXJfaWQiOiIyOSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNjk0YWUwNmRiMTA5ZGM3ZGE1NTkyNTNjZGRiMzg3MWVmYzFiN2VlNiIsIlBfaWQiOjEsIlBfbmFtZSI6IlA1LVNpZ25hbGxpbmciLCJsb2dpbiI6InRydWUiLCJlbWFpbCI6IkdhYnJpZWxAZ21haWwuY29tIiwidXNlcl9Sb2xlIjozLCJ1c2VyX0lEIjoyOX0=	2022-02-03 08:44:36.266097+00
1hvwc1ydmn7oguwz5rus5czjhviwx9s1	M2RiNzE3ZmFiNzQzOWVmNzg2Y2IzNGVkYzExM2E3NzM2YmVkZDI3ODp7Il9hdXRoX3VzZXJfaWQiOiIzOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiM2E3ZTE5YjUyODUzMGQ3YWJmYWM4YzVkNmI1NzkwM2E0N2MwZWFhYiIsIlBfaWQiOjEsIlBfbmFtZSI6IlA1LVNpZ25hbGxpbmciLCJsb2dpbiI6InRydWUiLCJlbWFpbCI6InNhbUBnbWFpbC5jb20iLCJ1c2VyX1JvbGUiOjQsInVzZXJfSUQiOjM4fQ==	2022-02-03 10:27:59.880946+00
011ml5guvqjaesqe1htp7ewkiqbc1u49	YjE1OWQ3OWZlMjU0YjE5OTllMmY0Yjk2NmJiZjYzNjQzY2MxZWFhMzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMGY0NDQ3NDNlNmI3M2IyOTlkZjY5MjY0NjUzYmFlZDlhYzFlYTI5ZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2022-02-03 12:02:14.53052+00
na84owpcs3t7ga0yrew9tfbmvo015bwv	YjE1OWQ3OWZlMjU0YjE5OTllMmY0Yjk2NmJiZjYzNjQzY2MxZWFhMzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMGY0NDQ3NDNlNmI3M2IyOTlkZjY5MjY0NjUzYmFlZDlhYzFlYTI5ZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2022-02-04 07:57:35.349356+00
ydr91maigma2r0i6ltscvqi4qs67jyhi	YjE1OWQ3OWZlMjU0YjE5OTllMmY0Yjk2NmJiZjYzNjQzY2MxZWFhMzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMGY0NDQ3NDNlNmI3M2IyOTlkZjY5MjY0NjUzYmFlZDlhYzFlYTI5ZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2022-02-05 13:31:19.754652+00
5vgvrgau2edw97chqqf5z555f2szz9hg	YjE1OWQ3OWZlMjU0YjE5OTllMmY0Yjk2NmJiZjYzNjQzY2MxZWFhMzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMGY0NDQ3NDNlNmI3M2IyOTlkZjY5MjY0NjUzYmFlZDlhYzFlYTI5ZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2022-02-08 12:17:40.265556+00
gcrpvedggk3kmo84iidlw0ngkqcht45u	YjE1OWQ3OWZlMjU0YjE5OTllMmY0Yjk2NmJiZjYzNjQzY2MxZWFhMzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMGY0NDQ3NDNlNmI3M2IyOTlkZjY5MjY0NjUzYmFlZDlhYzFlYTI5ZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2022-02-09 15:41:35.69991+00
v06aecyc7b6tt4qtl2u2n26wtqbwysov	OGJlYWE1ZDA1ZjI4YjYzM2JiMjUzY2Q4MTM3NGZhODhjNmJjNjc0Yjp7Il9hdXRoX3VzZXJfaWQiOiIzMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiN2NhNWFlOTg2MGIwNzgxY2ExNTkyYTkwZGVkMjhjY2RlZjQxNTUwNyIsIlBfaWQiOjEsIlBfbmFtZSI6IlA1LVNpZ25hbGxpbmciLCJsb2dpbiI6InRydWUiLCJlbWFpbCI6IlN1aHVAZ21haWwuY29tIiwidXNlcl9Sb2xlIjoyLCJ1c2VyX0lEIjozMn0=	2022-02-15 10:57:14.327086+00
a51zc28c3zuwgd1qavpojiv65byfkg9u	YjE1OWQ3OWZlMjU0YjE5OTllMmY0Yjk2NmJiZjYzNjQzY2MxZWFhMzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMGY0NDQ3NDNlNmI3M2IyOTlkZjY5MjY0NjUzYmFlZDlhYzFlYTI5ZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2022-02-22 13:34:31.734237+00
fmzdevwxmbzx7b8xds5asv9nyba9b6y2	YjE1OWQ3OWZlMjU0YjE5OTllMmY0Yjk2NmJiZjYzNjQzY2MxZWFhMzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMGY0NDQ3NDNlNmI3M2IyOTlkZjY5MjY0NjUzYmFlZDlhYzFlYTI5ZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2022-02-22 14:46:41.496619+00
9b1ccec2jnvkb8irsnvxlit2wviv7sbc	YjE1OWQ3OWZlMjU0YjE5OTllMmY0Yjk2NmJiZjYzNjQzY2MxZWFhMzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMGY0NDQ3NDNlNmI3M2IyOTlkZjY5MjY0NjUzYmFlZDlhYzFlYTI5ZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2022-02-23 03:00:02.732174+00
l3lojj1pcfaajg3soz3iih80le735efi	YjE1OWQ3OWZlMjU0YjE5OTllMmY0Yjk2NmJiZjYzNjQzY2MxZWFhMzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMGY0NDQ3NDNlNmI3M2IyOTlkZjY5MjY0NjUzYmFlZDlhYzFlYTI5ZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2022-02-23 03:51:39.247373+00
pgnc5vnba4s3bl8zauz3ez9bva3t4qv2	YjE1OWQ3OWZlMjU0YjE5OTllMmY0Yjk2NmJiZjYzNjQzY2MxZWFhMzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMGY0NDQ3NDNlNmI3M2IyOTlkZjY5MjY0NjUzYmFlZDlhYzFlYTI5ZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2022-02-23 03:51:39.380341+00
5jnsp3ropzub91mfcb6kdo9z26hjrn7r	YjE1OWQ3OWZlMjU0YjE5OTllMmY0Yjk2NmJiZjYzNjQzY2MxZWFhMzp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMGY0NDQ3NDNlNmI3M2IyOTlkZjY5MjY0NjUzYmFlZDlhYzFlYTI5ZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2022-02-28 17:27:55.79599+00
mgrpdeyxtqzexlelronn1gpjmdgdndlq	.eJxVjrsKwjAUht8ls5RcaJt0EnFxEMQXKMk5J220TaCXSXx3U-mg43_le7HWrkvfrjNNbUDWMKnZ4dd0Fp4UtwQfNnapgBSXKbhiqxR7OhfXhDSc9u7fQW_nPq8VeVSEtuS1d0YAaQ3KoJBCl8JzAiMBsDJWuqr2HpzSQrnSgEZXA-f59PYl5Ac2pC7E_LlMK2WfRhuGLC2OIR67TWXKMSdfgHsaiDViV5cza6R-fwDvL1Ec:1nKwzP:Xafrpts0aQIaq5jNt6wValYguafUumxbouujIxXAHrg	2022-03-04 06:43:35.57178+00
1ps3mbmpv34y85tbm4omwraqwtzsi3g7	.eJxVjrsKwjAUht8ls5RcaJt0EnFxEMQXKMk5J220TaCXSXx3U-mg43_le7HWrkvfrjNNbUDWMKnZ4dd0Fp4UtwQfNnapgBSXKbhiqxR7OhfXhDSc9u7fQW_nPq8VeVSEtuS1d0YAaQ3KoJBCl8JzAiMBsDJWuqr2HpzSQrnSgEZXA-f59PYl5Ac2pC7E_LlMK2WfRhuGLC2OIR67TWXKMSdfgHsaiDViV5cza6R-fwDvL1Ec:1nSAwn:VSIJP7Klee3ty5U9Feo2Sh9r6W5XClb1Xfe-t0luK3Y	2022-03-24 05:02:45.410041+00
3gl8sq7h67yjemo7vjn9asxhdztgw64x	.eJxVjrsKwjAUht8ls5RcaJt0EnFxEMQXKMk5J220TaCXSXx3U-mg43_le7HWrkvfrjNNbUDWMKnZ4dd0Fp4UtwQfNnapgBSXKbhiqxR7OhfXhDSc9u7fQW_nPq8VeVSEtuS1d0YAaQ3KoJBCl8JzAiMBsDJWuqr2HpzSQrnSgEZXA-f59PYl5Ac2pC7E_LlMK2WfRhuGLC2OIR67TWXKMSdfgHsaiDViV5cza6R-fwDvL1Ec:1nWVtU:fvBV-PVQnxBOeMbWpEO6gfXBhqCesMv0rmsv7F9uHGk	2022-04-05 04:13:16.790697+00
z815ctt1na02ghnn87j8v1yf6w4ny51e	.eJxVjrsKwjAUht8ls5RcaJt0EnFxEMQXKMk5J220TaCXSXx3U-mg43_le7HWrkvfrjNNbUDWMKnZ4dd0Fp4UtwQfNnapgBSXKbhiqxR7OhfXhDSc9u7fQW_nPq8VeVSEtuS1d0YAaQ3KoJBCl8JzAiMBsDJWuqr2HpzSQrnSgEZXA-f59PYl5Ac2pC7E_LlMK2WfRhuGLC2OIR67TWXKMSdfgHsaiDViV5cza6R-fwDvL1Ec:1nWYla:WjaDQHVjGfrUqYc74DSNGcgKRoBX3wYI_4WynALAM8E	2022-04-05 07:17:18.639766+00
2febu6oirop2741vcwj8at8o29y9hsce	.eJxVjrsKwjAUht8ls5RcaJt0EnFxEMQXKMk5J220TaCXSXx3U-mg43_le7HWrkvfrjNNbUDWMKnZ4dd0Fp4UtwQfNnapgBSXKbhiqxR7OhfXhDSc9u7fQW_nPq8VeVSEtuS1d0YAaQ3KoJBCl8JzAiMBsDJWuqr2HpzSQrnSgEZXA-f59PYl5Ac2pC7E_LlMK2WfRhuGLC2OIR67TWXKMSdfgHsaiDViV5cza6R-fwDvL1Ec:1o1kRp:BAu0x6fEoZ38TxrYNI6bk6j49H6C-Z7lXUWXndBvzeg	2022-06-30 08:01:49.442982+00
4j7e3jv28q8qb7by9btog8axzcxw4vb8	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-03-15 05:33:43.72851+00
dlhkxm6d9kkgy3jk0107iugf4x134d70	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-04-04 04:53:50.338496+00
szf9b0tnhpwbgprmom0we4c5yq2q90pt	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-06-24 10:23:43.857477+00
pzd4k787xigqctautyxm4uvfkm86jl2o	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-07 05:05:24.967767+00
r9r5oxs5l9nxn1l0x1oxmv2tvy5hapf5	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-07 07:45:11.221344+00
fa8xwouivktgskqa1gr1iz9iipob8lno	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-07 08:06:21.306472+00
c1laheao36he3t0o6eflf8m3el7qwkpq	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-07 08:12:59.284605+00
s92a4xyxb4kut6yvy1p7xhm3sg7i507d	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-09 07:55:00.892596+00
69metx1545wve87bide1bo6n5wrbd4lb	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-10 05:44:38.78773+00
jmes9o3ljqgrx2ryt9obpgh4etc3gjnk	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-10 06:31:54.07001+00
furmvog1qwhivj3e10dpjwjc8a5np4ew	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-08-09 04:39:23.223883+00
leea3l0aoj43cwigjd1az51yjprhizmt	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-12 06:01:38.874142+00
5qhdq3joekoyue46jv8b9g0fs70jjk4e	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-21 09:17:10.175587+00
mepd1vhqnvv5p49aymt1p5uz3vdw9qaw	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-16 05:14:11.697346+00
nssjawvcq1d2lare7xb6fcb4hcxynech	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-21 09:19:17.659503+00
2yjeqtpz5sz4e6p2c0tmp1rw24jwcjmb	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-17 05:01:30.756717+00
tl7jo9e5cpwkpom26qc0ktxhdhd91ja6	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-23 11:37:09.010917+00
jh5d36usorx9h66oy6lbjw0u1hbge24v	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-23 11:48:42.013443+00
lsbnx7uhumhg78za2dnu375ch1vxzcme	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-24 04:06:10.193437+00
epn11drevtw02rovws634uzbiadmr43a	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-28 09:04:58.718228+00
b6uscewrmvcwysj5qliiboxy6v16uss4	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-28 09:33:37.007255+00
24111blkw9ok83eqm5uanyc8ym7rjuzm	NzY0OGU3ZDcwOTdlNmRmNzdmMmUxYjYyMGYwZTcyZDFmOWRmMGMzMzp7Il9hdXRoX3VzZXJfaWQiOiI0MSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMmJiOTZmZTMxMzExZDZkYTljNDlkOWUxZDc2YTVlODY5MTYyN2E5NyIsIlBfaWQiOjEwLCJQX25hbWUiOiJQdW5lTWV0cm8iLCJsb2dpbiI6InRydWUiLCJlbWFpbCI6InJhbUBnbWFpbC5jb20iLCJ1c2VyX1JvbGUiOjMsInVzZXJfSUQiOjQxfQ==	2025-07-17 12:49:12.100531+00
4r05zfic6o7rdp5jvime5imsxif9t7qn	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-28 10:50:29.549341+00
4pv5vsv1q2ycefbitlaj80ikeeper4cy	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-29 04:11:04.38944+00
q63ue4zl7b73vg7yzhypi9jrkvlgjmbg	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-29 04:31:26.427578+00
z1nzvzy7um258mzonhqa1idwazsv5lny	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-29 04:32:25.208898+00
r6a9g5fk5of06zvka3xpkeskllznn1vl	ODgyMzAxODQwMTdjNTcxOGU4MzMyMjM0ZTgwNWY4OWVhN2VmOWI5Yjp7Il9hdXRoX3VzZXJfaWQiOiI0MCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZmMzYjUxZmVlZmIxYmZhMWEyY2JhMmM2YmNiZDdlYTE0OWExNTQ3ZCIsIlBfaWQiOjEwLCJQX25hbWUiOiJQdW5lTWV0cm8iLCJsb2dpbiI6InRydWUiLCJlbWFpbCI6Im1haW50YWluZXJAZ21haWwuY29tIiwidXNlcl9Sb2xlIjo2LCJ1c2VyX0lEIjo0MH0=	2025-08-01 04:59:34.388888+00
00tubjznl5w1qs6ywy5jx3uufr9mik3m	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-08-11 04:57:58.348707+00
ia4gcyy4m6w3kckemimaus66vp2vow08	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-29 06:25:34.296349+00
9zknfk96kpstfjhwq62g9favaxkwovl1	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-30 07:08:24.774999+00
0pszwmgcm4dyqlwab5daqnsyfv1zowrp	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-30 08:53:36.891077+00
txdwelhhouwuahx2umivs1r3pbo9bvwg	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-07-30 10:00:06.656287+00
yz2u9xkjqzuw3z2wwlqss0n8ur2awqxg	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-08-18 04:50:00.042032+00
nikrsof8lt5g9bucyklonrrkb5oo0xet	ODgyMzAxODQwMTdjNTcxOGU4MzMyMjM0ZTgwNWY4OWVhN2VmOWI5Yjp7Il9hdXRoX3VzZXJfaWQiOiI0MCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZmMzYjUxZmVlZmIxYmZhMWEyY2JhMmM2YmNiZDdlYTE0OWExNTQ3ZCIsIlBfaWQiOjEwLCJQX25hbWUiOiJQdW5lTWV0cm8iLCJsb2dpbiI6InRydWUiLCJlbWFpbCI6Im1haW50YWluZXJAZ21haWwuY29tIiwidXNlcl9Sb2xlIjo2LCJ1c2VyX0lEIjo0MH0=	2025-08-06 09:39:46.302409+00
bwwbgqkaf75r605x8pyjo4mgu7qcxles	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-08-18 11:30:09.585126+00
coxk1uo4plwk4nja0a3sogkpiuc6qljd	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-08-06 11:35:12.456679+00
ygfmla77hsecig35eyzf6h64wqcsrwvm	OGJkN2I2YzE2YjY2MGQxYjFlM2Y5MGUyNGU4NzU2ZmMwZjNkZTBhNTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTMyNDI0NDAxZTZlY2ZmYTNiZjQwNTE3Y2JhMDg5YTJiZmZmOWNjZiIsIlBfaWQiOjAsImxvZ2luIjoidHJ1ZSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwidXNlcl9Sb2xlIjoxLCJ1c2VyX0lEIjoyOH0=	2025-08-15 09:05:26.572716+00
\.


--
-- Data for Name: fracas_action; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_action (action_id, action_description, action_owner, action_status, action_due_date, progress_log, defect_discussion_id_id) FROM stdin;
\.


--
-- Data for Name: fracas_asset; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_asset (id, asset_config_id, location_id, location_description, asset_serial_number, asset_type, asset_description, software_version, software_description, asset_status, is_active, "P_id", sub_location) FROM stdin;
1771	Asset_1	TS#24	Car name	TOST_6	383	Camera used rolling stock			ACTIVE	1	10	DMB
1772	Asset_2	TS#24	car number	TOST_5	407	Saloon door 			ACTIVE	1	10	DMB
1817	Asset 57 	TS#21	TS#21	TCMS-21	395	TCMS			ACTIVE	0	10	TS#21
1959	Asset-14	TS#02	TS# 02	BECU-02	365	BECU			ACTIVE	0	10	TS# 02
1983	Asset 68 	TS#29	TS#29	BECU-29	365	BECU			ACTIVE	0	10	TS#29
1961	Asset 21	TS#02	TS# 02	BECU-02	365	BECU			ACTIVE	1	10	TS# 02
1963	Asset-18	TS#14	TS#14	HVAC-14	421	HVAC			ACTIVE	0	10	TS#14
1818	Asset 59 	TS#23	TS#23	MDS -23	429	MDS			ACTIVE	0	10	TS#23
1773	Asset-01	TS#01	TS#01	BECU-01	365	BECU			ACTIVE	1	10	TS#01
1774	Asset-02	TS#01	TS#01	HVAC-01	421	HVAC			ACTIVE	1	10	TS#01
1775	Asset-03	TS#12	TS#12	DCU-12	418	DCU			ACTIVE	1	10	TS#12
1776	Asset-04	TS#12	TS#12	SUC-12	398	SUC			ACTIVE	1	10	TS#12
1777	Asset-05	TS#12	TS#12	MDS-12	429	MDS			ACTIVE	1	10	TS#12
1778	Asset-06	TS#12	TS#12	DRM-12	417	DRM			ACTIVE	1	10	TS#12
1779	Asset-07	TS#28	TS#28	DCU-28	418	DCU			ACTIVE	1	10	TS#28
1780	Asset-08	TS#28	TS#28	SUC-28	398	SUC			ACTIVE	1	10	TS#28
1781	Asset-09	TS#27	TS#28	MDS-28	429	MDS			ACTIVE	1	10	TS#28
1782	Asset-10	TS#28	TS#28	DRM-28	417	DRM			ACTIVE	1	10	TS#28
1783	Asset-11	TS#23	TS#23	Camera-23	386	Camera			ACTIVE	1	10	TS#23
1784	Asset-12	TS#07	TS#07	TCMS-7	395	TCMS			ACTIVE	1	10	TS#07
1785	Asset-1	TS#21	TS#21	CI 2 - 21	414	CI 2 			ACTIVE	0	10	TS#21
1786	Asset 3 	TS#25	TS#25	CI 2 - 25 	414	CI 2 			ACTIVE	0	10	TS#25 
1787	Asset 5	TS#26	TS #26	Cl 2 - 26	414	Cl 2 			ACTIVE	0	10	TS #26
1788	Asset 7 	TS#22	TS#22	CI 2 -22	414	CI-2			ACTIVE	0	10	TS#22
1789	Asset 9 	TS#16	TS#16	Cl 2 - 16	414	CI -2 			ACTIVE	0	10	TS#16
1791	Asset 13 	TS#08	TS# 08	Cab Door - 08	403	Cab Door 			ACTIVE	0	10	TS# 08
1792	Asset 15 	TS#09	TS#09 	Saloon Door - 09	407	Saloon Door 			ACTIVE	0	10	TS#09 
1793	Asset 17 	TS#25	TS#25	PA/PIS - 25	433	PA/PIS			ACTIVE	0	10	TS#25
1794	Asset 19 	TS#26	TS#26	PA/PIS - 26	433	PA/PIS			ACTIVE	0	10	TS#26
1795	Asset 21 	TS#26	TS#26	Breaker loop -26	368	Breaker loop			ACTIVE	0	10	TS#26
1796	Asset 23 	TS#24	TS#24\n	Brake -24	369	Braking 			ACTIVE	0	10	TS#24 
1797	Asset 25	TS#25	TS#25	Partion Door -25	404	Partion Door 			ACTIVE	0	10	TS#25
1798	Asset 27 	TS#07	TS#07	DRM - 07	417	DRM			ACTIVE	0	10	TS#07
1799	Asset 29 	TS#10	TS#10	PA/PIS - 10	433	PA/PIS 			ACTIVE	0	10	TS#10
1800	Asset 31	TS#07	TS#07	Compressor -07	371	Compressor			ACTIVE	0	10	TS#07
1801	Asset 33 	TS#21	TS#21	HVAC Unit 01 - 21	420	HVAC Unit 01 			ACTIVE	0	10	TS#21
1802	Asset 35 	TS#21	TS#21	HVAC Unit 02 - 21	419	HVAC Unit 02			ACTIVE	0	10	TS#21
1803	Asset 37 	TS#24	TS#24	PA/PIS -24	433	PA/PIS 			ACTIVE	0	10	TS#24
1804	Asset 39 	TS#26	TS#26	MDS/CCTV-26	428	MDS/CCTV			ACTIVE	0	10	TS#26
1805	Asset 41 	TS#08	TS#08	CL 2 -08	414	CL 2			ACTIVE	0	10	TS#08
1806	Asset 43 	TS#16	TS#16	HVAC Unit 01 -16	420	HVAC Unit 01 			ACTIVE	0	10	TS#16
1807	Asset 45	TS#24	TS#24	TCMS-24	395	TCMS-24			ACTIVE	0	10	TS#24
1808	Asset-2	TS#05	TS#05	HVAC-05	421	HVAC			ACTIVE	0	10	TS#05
1809	Asset 47 	TS#25	TS#25	TCMS-25	395	TCMS			ACTIVE	0	10	TS#25
1810	Asset 49	TS#25	TS#25	Saloon Door - 25	407	Saloon Door 			ACTIVE	0	10	TS#25
1811	Asset 51 	TS#15	TS#15	HVAC Unit 02 -15	419	HVAC Unit 02 			ACTIVE	0	10	TS#15
1812	Asset-4	TS#03	TS#03	HVAC-03	421	HVAC			ACTIVE	0	10	TS#03
1813	Asset-6	TS#03	TS#03	BECU-03	365	BECU			ACTIVE	0	10	TS#03
1814	Asset 53 	TS#26	TS#26	Announcement - 26	415	Announcement 			ACTIVE	0	10	TS#26
1815	Asset-8	TS#03	TS#03	CI-03	412	CI			ACTIVE	0	10	TS#03
1816	Asset 55 	TS#07	TS#07	TCMS-07	395	TCMS			ACTIVE	0	10	TS#07
1965	Asset-22	TS#20	TS#20	BECU-20	365	BECU			ACTIVE	0	10	TS#20
1967	Asset-26	TS#28	TS#28	Cab Door-28	403	Cab Door			ACTIVE	0	10	TS#28
1969	Asset-30	TS#27	TS#27	HVAC-27	421	HVAC			ACTIVE	0	10	TS#27
1971	Asset-34	TS#19	TS#19	Battery-19	352	Battery			ACTIVE	0	10	TS#19
1973	Asset 38	TS#26	TS#26	Car Door-26	406	Car Door			ACTIVE	0	10	TS#26
1975	Asset 80 	TS#13	TS#13	FDU-13	426	FDU			ACTIVE	0	10	TS#13
1977	Asset 40	TS#25	TS#25	Car Door-25	406	Car Door			ACTIVE	0	10	TS#25
1979	Asset 76 	TS#06	TS#06	FDU-06	426	FDU			ACTIVE	0	10	TS#06
1981	Asset 70	TS#17	TS#17	Cab Door-17	403	Cab Door			ACTIVE	0	10	TS#17
1985	Asset 46	TS#04	TS#04	HVAC-04	421	HVAC			ACTIVE	0	10	TS#04
1829	Asset 61 	TS#07	TS#07	Battery -07	352	Battery			ACTIVE	0	10	TS#07
1830	Asset 63 	TS#07	TS#07	SDU-07	396	SDU			ACTIVE	0	10	TS#07
1831	Asset 65 	TS#26	TS#26	Partion Door- 26	404	Partion Door			ACTIVE	0	10	TS#26
1987	Asset 50	TS#07	TS#07	Pantograph-07	388	Pantograph			ACTIVE	0	10	TS#07
1989	Asset 54	TS#24	TS#24	VCC-24	392	VCC			ACTIVE	0	10	TS#24
1991	Asset 58	TS#21	TS#21	MDS-21	429	MDS			ACTIVE	0	10	TS#21
1993	Asset 64	TS#30	TS#30	BECU-30	365	BECU			ACTIVE	0	10	TS#30
1867	Asset 81 	TS#09	TS#09	Announcement-09	415	Announcement-09			ACTIVE	0	10	TS#09
1960	Asset-21	TS#02	TS# 02	BECU-02	365	BECU			ACTIVE	1	10	TS# 02
1855	Asset 67 	TS#08	TS#08	TCMS-08	395	TCMS			ACTIVE	0	10	TS#08
1857	Asset 71 	TS#18	TS#18	TCMS-18	395	TCMS			ACTIVE	0	10	TS#18
1858	Asset 73	TS#15	TS#15	TCMS-15	395	TCMS-15			ACTIVE	0	10	TS#15
1856	Asset 69 	TS#09	TS#09	TCMS-09	395	TCMS			ACTIVE	0	10	TS#09
1962	Asset-16	TS#12	TS#12	MDS-12	429	MDS			ACTIVE	0	10	TS#12
1964	Asset-20	TS#14	TS#14	Wiper-14	424	Wiper			ACTIVE	0	10	TS#14
1966	Asset-24	TS#20	TS#20	FDU-20	426	FDU			ACTIVE	0	10	TS#20
1968	Asset-28	TS#25	TS#25	CCTV-25	385	CCTV			ACTIVE	0	10	TS#25
1864	Asset 75	TS#26	TS#26	Battery -26	352	Battery			ACTIVE	0	10	TS#26
1865	Asset 77 	TS#25	TS#25	HVAC Unit 02 -25	419	HVAC Unit 02 			ACTIVE	0	10	TS#25
1866	Asset 79 	TS#25	TS#25	EB Push Button-25	405	EB Push Button			ACTIVE	0	10	TS#25
1868	Asset 83	TS#23	TS#23	CCTV-23	385	CCTV			ACTIVE	0	10	TS#23
1970	Asset-32	TS#06	TS#06	Saloon Door-06	407	Saloon Door			ACTIVE	0	10	TS#06
1972	Asset-36	TS#06	TS#06	DCU-06	418	DCU			ACTIVE	0	10	TS#06
1974	Asset 82 	TS#19	TS#13	HVAC Unit 02 - 13 	419	HVAC Unit 02			ACTIVE	0	10	TS#13
1976	Asset 78 	TS#05	TS#05	FDU-5	426	FDU			ACTIVE	0	10	TS#05
1978	Asset 42	TS#23	TS#23	HVAC Unit 2-23	419	HVAC			ACTIVE	0	10	TS#23
1980	Asset 74 	TS#06	TS#06	MDS-06	429	MDS			ACTIVE	0	10	TS#06
1982	Asset 70 	TS#20	TS#20	Announcement-20	415	Announcement			ACTIVE	0	10	TS#20
1986	Asset 48	TS#24	TS#24	HVAC-24	421	HVAC			ACTIVE	0	10	TS#24
1988	Asset 52	TS#09	TS#09	Emergency Door-09	402	Emergency Door			ACTIVE	0	10	TS#09
1990	Asset 56	TS#21	TS#21	PA/PIS-21	433	PA/PIS			ACTIVE	0	10	TS#21
1984	Asset 66	TS#02	TS#02	BECU-02	365	BECU			ACTIVE	1	10	TS#02
1992	Asset 62	TS#30	TS#30	MDS-30	429	MDS			ACTIVE	0	10	TS#30
1790	Asset 11 	TS#24	TS#24 	Announcement/TS#24/TC/001	415	Announcement 			ACTIVE	0	10	TC
\.


--
-- Data for Name: fracas_assetregister; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_assetregister (id) FROM stdin;
\.


--
-- Data for Name: fracas_assetserialnumberids; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_assetserialnumberids (uid_id, asset_type, location_id, sub_location, last_id) FROM stdin;
\.


--
-- Data for Name: fracas_correctiveaction; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_correctiveaction (corrective_action_id, corrective_action_owner, corrective_action_description, corrective_action_update, corrective_action_status, defect_id, "P_id", is_active) FROM stdin;
128	Relay OEM 	corrective action 	corrective action	Monitoring	189	10	0
129	maintainer	motor is not working	rubber was removed from bearing of motor	Open	191	10	0
130	maintainer	cleaned the filter	on sight cleaning done. 	Resolved	192	10	0
131	*Corrective action owner:	*Corrective action description:	*Corrective action update:	Open	193	10	0
\.


--
-- Data for Name: fracas_defect; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_defect (start_date, end_date, asset_type, defect_id, defect_description, defect_open_date, defect_closed_date, investigation, defect_status, defect_status_remarks, oem_defect_reference, oem_target_date, "P_id", is_active) FROM stdin;
2024-08-01	2024-09-30	421	190		\N	\N					\N	10	0
2024-08-01	2024-09-01	414	189	defect	2024-08-01	2024-09-01	investigation 		open	oem defect	2025-07-24	10	0
2024-08-01	2024-09-10	421	191	HVAC not working	2024-09-30	\N	Motor found faulty	Open	open 		2025-07-30	10	0
2024-08-01	2024-09-10	421	192	filter grill is defected	2025-07-31	\N	inspection	Open	open 		2025-08-05	10	0
2024-07-31	2024-08-01	421	193	*Defect description:	2025-07-25	\N	\n*Defect description:\n*Investigation:	Open	Defect status remarks		2025-12-18	10	0
2024-08-01	2024-09-10	421	194	sgshsh	2025-07-10	\N	snananb	Open	open		2025-08-31	10	0
\.


--
-- Data for Name: fracas_defectdiscussion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_defectdiscussion (defect_discussion_id, meeting_date, defect_id, review_board_id, description) FROM stdin;
79	2025-07-18	189	82	
80	2025-07-18	189	82	
\.


--
-- Data for Name: fracas_defectdiscussion_attendees; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_defectdiscussion_attendees (id, defectdiscussion_id, userprofile_id) FROM stdin;
66	79	28
67	80	26
\.


--
-- Data for Name: fracas_eirgeneration; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_eirgeneration (eir_id, depot, addressed_by, incident_details, repercussion, incident_location, incident_time, failure_id_id, eir_gen_id, component, action_taken_in_depot, concern, further_action, "TRSL", signature_img2, signature_img3) FROM stdin;
60	HVPCD	Mahtab	air filter was damaged 	None	Depot	10:30	28806	Maha Metro/RS/2025/0060	filter	None	None	None	None	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg
1	RHD	None	Incident Details	Repercussion:	Depot	15:44	28747	Maha Metro/RS/2025/0001	Component:	None	None	None	None	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg
2	\N	\N	\N	\N	\N	\N	28748	Maha Metro/RS/2025/0002	\N	\N	\N	\N	\N	\N	\N
3	\N	\N	\N	\N	\N	\N	28749	Maha Metro/RS/2025/0003	\N	\N	\N	\N	\N	\N	\N
4	\N	\N	\N	\N	\N	\N	28750	Maha Metro/RS/2025/0004	\N	\N	\N	\N	\N	\N	\N
5	\N	\N	\N	\N	\N	\N	28751	Maha Metro/RS/2025/0005	\N	\N	\N	\N	\N	\N	\N
6	\N	\N	\N	\N	\N	\N	28752	Maha Metro/RS/2025/0006	\N	\N	\N	\N	\N	\N	\N
7	\N	\N	\N	\N	\N	\N	28753	Maha Metro/RS/2025/0007	\N	\N	\N	\N	\N	\N	\N
8	\N	\N	\N	\N	\N	\N	28754	Maha Metro/RS/2025/0008	\N	\N	\N	\N	\N	\N	\N
9	\N	\N	\N	\N	\N	\N	28755	Maha Metro/RS/2025/0009	\N	\N	\N	\N	\N	\N	\N
10	\N	\N	\N	\N	\N	\N	28756	Maha Metro/RS/2025/0010	\N	\N	\N	\N	\N	\N	\N
11	\N	\N	\N	\N	\N	\N	28757	Maha Metro/RS/2025/0011	\N	\N	\N	\N	\N	\N	\N
12	\N	\N	\N	\N	\N	\N	28758	Maha Metro/RS/2025/0012	\N	\N	\N	\N	\N	\N	\N
13	\N	\N	\N	\N	\N	\N	28759	Maha Metro/RS/2025/0013	\N	\N	\N	\N	\N	\N	\N
14	\N	\N	\N	\N	\N	\N	28760	Maha Metro/RS/2025/0014	\N	\N	\N	\N	\N	\N	\N
15	\N	\N	\N	\N	\N	\N	28761	Maha Metro/RS/2025/0015	\N	\N	\N	\N	\N	\N	\N
16	\N	\N	\N	\N	\N	\N	28762	Maha Metro/RS/2025/0016	\N	\N	\N	\N	\N	\N	\N
17	\N	\N	\N	\N	\N	\N	28763	Maha Metro/RS/2025/0017	\N	\N	\N	\N	\N	\N	\N
19	\N	\N	\N	\N	\N	\N	28765	Maha Metro/RS/2025/0019	\N	\N	\N	\N	\N	\N	\N
20	\N	\N	\N	\N	\N	\N	28766	Maha Metro/RS/2025/0020	\N	\N	\N	\N	\N	\N	\N
21	\N	\N	\N	\N	\N	\N	28767	Maha Metro/RS/2025/0021	\N	\N	\N	\N	\N	\N	\N
22	\N	\N	\N	\N	\N	\N	28768	Maha Metro/RS/2025/0022	\N	\N	\N	\N	\N	\N	\N
23	\N	\N	\N	\N	\N	\N	28769	Maha Metro/RS/2025/0023	\N	\N	\N	\N	\N	\N	\N
24	\N	\N	\N	\N	\N	\N	28770	Maha Metro/RS/2025/0024	\N	\N	\N	\N	\N	\N	\N
25	\N	\N	\N	\N	\N	\N	28771	Maha Metro/RS/2025/0025	\N	\N	\N	\N	\N	\N	\N
26	\N	\N	\N	\N	\N	\N	28772	Maha Metro/RS/2025/0026	\N	\N	\N	\N	\N	\N	\N
27	\N	\N	\N	\N	\N	\N	28773	Maha Metro/RS/2025/0027	\N	\N	\N	\N	\N	\N	\N
28	\N	\N	\N	\N	\N	\N	28774	Maha Metro/RS/2025/0028	\N	\N	\N	\N	\N	\N	\N
29	\N	\N	\N	\N	\N	\N	28775	Maha Metro/RS/2025/0029	\N	\N	\N	\N	\N	\N	\N
30	\N	\N	\N	\N	\N	\N	28776	Maha Metro/RS/2025/0030	\N	\N	\N	\N	\N	\N	\N
31	\N	\N	\N	\N	\N	\N	28777	Maha Metro/RS/2025/0031	\N	\N	\N	\N	\N	\N	\N
32	\N	\N	\N	\N	\N	\N	28778	Maha Metro/RS/2025/0032	\N	\N	\N	\N	\N	\N	\N
33	\N	\N	\N	\N	\N	\N	28779	Maha Metro/RS/2025/0033	\N	\N	\N	\N	\N	\N	\N
34	\N	\N	\N	\N	\N	\N	28780	Maha Metro/RS/2025/0034	\N	\N	\N	\N	\N	\N	\N
35	\N	\N	\N	\N	\N	\N	28781	Maha Metro/RS/2025/0035	\N	\N	\N	\N	\N	\N	\N
36	\N	\N	\N	\N	\N	\N	28782	Maha Metro/RS/2025/0036	\N	\N	\N	\N	\N	\N	\N
37	\N	\N	\N	\N	\N	\N	28783	Maha Metro/RS/2025/0037	\N	\N	\N	\N	\N	\N	\N
38	\N	\N	\N	\N	\N	\N	28784	Maha Metro/RS/2025/0038	\N	\N	\N	\N	\N	\N	\N
39	\N	\N	\N	\N	\N	\N	28785	Maha Metro/RS/2025/0039	\N	\N	\N	\N	\N	\N	\N
40	\N	\N	\N	\N	\N	\N	28786	Maha Metro/RS/2025/0040	\N	\N	\N	\N	\N	\N	\N
41	\N	\N	\N	\N	\N	\N	28787	Maha Metro/RS/2025/0041	\N	\N	\N	\N	\N	\N	\N
42	\N	\N	\N	\N	\N	\N	28788	Maha Metro/RS/2025/0042	\N	\N	\N	\N	\N	\N	\N
43	\N	\N	\N	\N	\N	\N	28789	Maha Metro/RS/2025/0043	\N	\N	\N	\N	\N	\N	\N
44	\N	\N	\N	\N	\N	\N	28790	Maha Metro/RS/2025/0044	\N	\N	\N	\N	\N	\N	\N
45	\N	\N	\N	\N	\N	\N	28791	Maha Metro/RS/2025/0045	\N	\N	\N	\N	\N	\N	\N
46	\N	\N	\N	\N	\N	\N	28792	Maha Metro/RS/2025/0046	\N	\N	\N	\N	\N	\N	\N
47	\N	\N	\N	\N	\N	\N	28793	Maha Metro/RS/2025/0047	\N	\N	\N	\N	\N	\N	\N
48	\N	\N	\N	\N	\N	\N	28794	Maha Metro/RS/2025/0048	\N	\N	\N	\N	\N	\N	\N
49	\N	\N	\N	\N	\N	\N	28795	Maha Metro/RS/2025/0049	\N	\N	\N	\N	\N	\N	\N
50	\N	\N	\N	\N	\N	\N	28796	Maha Metro/RS/2025/0050	\N	\N	\N	\N	\N	\N	\N
51	\N	\N	\N	\N	\N	\N	28797	Maha Metro/RS/2025/0051	\N	\N	\N	\N	\N	\N	\N
52	\N	\N	\N	\N	\N	\N	28798	Maha Metro/RS/2025/0052	\N	\N	\N	\N	\N	\N	\N
53	\N	\N	\N	\N	\N	\N	28799	Maha Metro/RS/2025/0053	\N	\N	\N	\N	\N	\N	\N
54	\N	\N	\N	\N	\N	\N	28800	Maha Metro/RS/2025/0054	\N	\N	\N	\N	\N	\N	\N
55	\N	\N	\N	\N	\N	\N	28801	Maha Metro/RS/2025/0055	\N	\N	\N	\N	\N	\N	\N
56	\N	\N	\N	\N	\N	\N	28802	Maha Metro/RS/2025/0056	\N	\N	\N	\N	\N	\N	\N
57	\N	\N	\N	\N	\N	\N	28803	Maha Metro/RS/2025/0057	\N	\N	\N	\N	\N	\N	\N
58	\N	\N	\N	\N	\N	\N	28804	Maha Metro/RS/2025/0058	\N	\N	\N	\N	\N	\N	\N
18	\N	\N	\N	\N	\N	\N	28764	Maha Metro/RS/2025/0018	\N	None	None	None	None	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg
59	RHD	Amir	not working 	no climate control in the train. 	Depot	None	28805	Maha Metro/RS/2025/0059	Motor	None	None	None	None	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg
\.


--
-- Data for Name: fracas_eirids; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_eirids (uid_id, year, last_id) FROM stdin;
1	2025	60
\.


--
-- Data for Name: fracas_eirimages; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_eirimages (img_id, file_path, is_active, eir_dt_id_id) FROM stdin;
1	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	0	1
2	/home/assetoptima/pune_metro_jobcard/static/uploads/png.png	0	18
3	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	0	59
4	/home/assetoptima/pune_metro_jobcard/static/uploads/Screenshot 2025-06-19 at 2.00.47 PM (1).png	0	60
\.


--
-- Data for Name: fracas_employeemaster; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_employeemaster (id, employee_id, name, designation) FROM stdin;
\.


--
-- Data for Name: fracas_failuredata; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_failuredata (id, failure_id, event_description, date, "time", detection, service_delay, immediate_investigation, failure_type, safety_failure, hazard_id, cm_description, replaced_asset_config_id, cm_start_date, cm_start_time, cm_end_date, cm_end_time, oem_failure_reference, asset_config_id_id, defect_id, mode_description, mode_id_id, asset_type, "P_id", is_active, "TO_name", department, direction, equipment, kilometre_reading, location, location_id, no_of_trip_cancel, "reported_to_PPIO", sel_car, incident, deboarding) FROM stdin;
28745	RST/06-2025/230829395LPSO	camera isnt working	2025-06-23	15:03:00	Inspection	15	inspected and replaced 	Hardware	Yes		 part is replaced	222630	2025-06-04	16:11:00	2025-06-04	16:21:00		Asset_1	\N	\N	\N	383	10	1	ramesh	Operator	Up	camera	255562	HPD	1771	0	Yes	DMA, TC, DMB	Yes	No
28747	RST/06-2025/FID_0001	DMB air dryer fault coming continuously and buzzer ringing frequently	2025-06-25	15:23:00	Inspection	0	*Immediate Action Taken:	Software	Yes		*Cm description:		2025-06-25	15:23:00	2025-06-25	15:23:00		Asset_1	\N	\N	\N	383	10	1	alana 	Operator	Up	camera	255562	HPD	1771	1	Yes	DMA	Yes	Yes
28746	RST/06-2025/231037084Y0RL	door hinges fail	2025-06-23	16:07:00	Inspection	0	oiled the hinge	Hardware	Yes		changing of hinge 		2025-06-25	12:09:00	2025-06-25	14:10:00		Asset_1	\N	\N	\N	383	10	1	ramesh	Operator	Up	Hinge 	36552	HPD	1771	0	Yes	TC	Yes	No
28748	RST/06-2025/FID_0002	DMB air dryer fault coming continuously and buzzer ringing frequently	2025-06-27	12:30:00	Inspection	0	immediate 	Hardware	Yes		cm disc		2025-06-27	12:30:00	2025-06-27	12:40:00		Asset_1	\N	\N	\N	383	10	1	alana 	Operator	Up	Lense	255562	HPD	1771	1	Yes	TC	Yes	Yes
28759	RST/07-2025/FID_0011	MDS Failure	2024-08-15	00:30:00	Inspection	10	Train service stops	Hardware	Yes		PAPIS software updated		2024-08-15	01:00:00	2024-08-15	01:10:00		Asset-09	\N	\N	\N	429	10	1	Ashik	Operator	Up	DCU	6253	TS#28	1781	0	Yes	DMA, TC, DMB	Yes	Yes
28760	RST/07-2025/FID_0012	DRM Failure	2024-08-15	00:30:00	Inspection	10	Train service stops	Hardware	Yes		PAPIS software updated		2024-08-15	01:00:00	2024-08-15	01:10:00		Asset-10	\N	\N	\N	417	10	1	Ashik	Operator	Up	DRM	6195	TS#28	1782	0	Yes	DMA, TC, DMB	Yes	Yes
28764	RST/07-2025/FID_0016	test2 	2025-07-03	11:31:00	Inspection	0	none	Software	Yes		none		2025-07-04	11:31:00	2025-07-04	11:31:00		Asset-11	\N	\N	\N	386	10	1	mihir	Operator	Up	camera	0	TS#23	1783	0	Yes	DMA	Yes	Yes
28754	RST/07-2025/FID_0006	SCU Failure	2024-08-15	00:30:00	Inspection	10	Train service stop	Hardware	Yes		PAPIS software updated		2024-08-15	01:00:00	2024-08-15	01:10:00		Asset-04	\N	\N	\N	398	10	1	Ashik	Operator	Up	SCU	80276	TS#12	1776	0	Yes	DMA, TC, DMB	Yes	Yes
28755	RST/07-2025/FID_0007	MDS Failure	2024-08-15	00:30:00	Inspection	10	Train service stops	Hardware	Yes		PAPIS Software update		2024-08-15	01:00:00	2024-08-15	01:10:00		Asset-05	\N	\N	\N	429	10	1	Ashik	Operator	Up	MDS	80276	TS#12	1777	0	Yes	DMA, TC, DMB	Yes	Yes
28756	RST/07-2025/FID_0008	DRM Failure	2024-08-15	00:30:00	Inspection	10	Train service stops	Hardware	Yes		PAPIS software updated		2024-08-15	01:00:00	2024-08-15	01:10:00		Asset-06	\N	\N	\N	417	10	1	Ashik	Operator	Up	DRM	80276	TS#12	1778	0	Yes	DMA, TC, DMB	Yes	Yes
28757	RST/07-2025/FID_0009	DCU Failure	2024-08-15	00:30:00	Inspection	10	Train service stops	Hardware	Yes		PAPIS software updated		2024-08-15	01:00:00	2024-08-15	01:10:00		Asset-07	\N	\N	\N	418	10	1	Ashik	Operator	Up	DCU	6195	TS#28	1779	0	Yes	DMA, TC, DMB	Yes	Yes
28761	RST/07-2025/FID_0013	CCTV Camera failure	2024-08-23	05:00:00	Inspection	30	Water accumulated in camera	Hardware	Yes		Camera cleaned and installed		2024-08-23	05:00:00	2024-08-23	05:30:00		Asset-11	\N	\N	\N	386	10	1	Ashik	Operator	Up	Camera	0	TS#23	1783	0	Yes	DMB	Yes	Yes
28749	RST/07-2025/FID_0001	Line fault lamp glowing but VCB not tripped, line voltage available. No line fault message pop up on TCMS	2024-08-28	09:30:00	Inspection	30	Train service stops and inspection	Hardware	Yes		Replaced the defective components		2024-08-28	10:00:00	2024-08-28	10:30:00		Asset-12	\N	\N	\N	395	10	1	Ashik	Operator	Up	TCMS	0	TS#07	1784	0	Yes	DMA	Yes	Yes
28750	RST/07-2025/FID_0002	BECU Failure	2024-08-19	16:28:00	Inspection	20	Train service stop	Hardware	Yes		Replaced the defective component		2024-08-19	16:30:00	2024-08-19	17:00:00		Asset-01	\N	\N	\N	365	10	1	Ashik	Operator	Up	BECU	123994	TS#01	1773	0	Yes	DMA, DMB	Yes	Yes
28751	RST/07-2025/FID_0003	BECU Component failure	2024-08-19	16:28:00	Inspection	20	Train service stop	Hardware	Yes		L13 magnetic valve protection cap installed		2024-08-19	16:30:00	2024-08-19	17:00:00		Asset-01	\N	\N	\N	365	10	1	Ashik	Operator	Up	BECU	123994	TS#01	1773	0	Yes	DMA, TC, DMB	Yes	Yes
28752	RST/07-2025/FID_0004	Failure of HVAC in drainage pipe	2024-08-19	16:28:00	Inspection	20	Train service stop	Hardware	Yes		HVAC drainage pipe extension hose pipe cleaned		2024-08-19	16:30:00	2024-08-19	17:00:00		Asset-02	\N	\N	\N	421	10	1	Ashik	Operator	Up	HVAC	123994	TS#01	1774	0	Yes	DMA, TC, DMB	Yes	Yes
28753	RST/07-2025/FID_0005	DCU component failure	2024-08-15	00:30:00	Inspection	10	Train service stops	Hardware	Yes		PAPIS Software updated		2024-08-15	01:00:00	2024-08-15	01:10:00		Asset-03	\N	\N	\N	418	10	1	Ashik	Operator	Up	DCU	80276	TS#12	1775	0	Yes	DMA, TC, DMB	Yes	Yes
28758	RST/07-2025/FID_0010	SCU Failure	2024-08-15	00:30:00	Inspection	10	Train service stops	Hardware	Yes		PAPIS software updated		2024-08-15	01:10:00	2024-08-15	01:10:00		Asset-08	\N	\N	\N	398	10	1	Ashik	Operator	Up	DCU	6195	TS#28	1780	0	Yes	DMA, TC, DMB	Yes	Yes
28762	RST/07-2025/FID_0014	test	2024-08-19	09:46:00	Inspection	20	Nil	Hardware	Yes		Nil		2024-08-19	10:00:00	2024-08-19	10:20:00		Asset-03	\N	\N	\N	418	10	1	Ashik	Operator	Up	DCU	81121	TS#12	1775	0	Yes	DMA	Yes	Yes
28763	RST/07-2025/FID_0015	test1	2025-07-03	11:06:00	Inspection	10	none	Software	Yes		none		2025-07-04	11:06:00	2025-07-04	11:06:00		Asset-03	\N	\N	\N	418	10	1	Mihir	Operator	Up	camera	100	TS#12	1775	0	Yes	DMA	Yes	Yes
28766	RST/07-2025/FID_0018	CI-2 	2024-08-15	22:30:00	Inspection	10	nil 	Hardware	Yes		TCMS Data download 		2024-08-15	22:40:00	2024-08-15	22:50:00		Asset 3 	189	\N	\N	414	10	0	Mihir	Maintainer	Up	CI-2	25000	TS#25	1786	0	Yes	DMA	Yes	Yes
28770	RST/07-2025/FID_0022	Partition Door 	2024-08-28	22:20:00	Inspection	10	nil	Hardware	Yes		DMA partition door is not closing properly 		2024-08-28	22:30:00	2024-08-28	22:40:00		Asset 25	\N	\N	\N	404	10	0	mihir	Maintainer	Up	Partition Door 	0	TS#25	1797	0	Yes	DMA	Yes	Yes
28771	RST/07-2025/FID_0023	Compressor 	2024-09-08	10:10:00	Inspection	10	nil	Hardware	Yes		Compressor oil change 		2024-09-08	10:10:00	2024-09-08	10:20:00		Asset 31	\N	\N	\N	371	10	0	mihir	Operator	Up	Compressor 	129086	TS#07	1800	0	Yes	DMA, DMB	Yes	Yes
28781	RST/07-2025/FID_0033	TCMS	2024-08-13	22:30:00	Inspection	10	nil	Hardware	Yes		TCMS data download 		2024-08-13	22:40:00	2024-08-13	22:50:00		Asset 47 	\N	\N	\N	395	10	0	mihir	Operator	Up	TCMS	25000	TS#25	1809	0	Yes	DMA	Yes	Yes
28801	RST/07-2025/FID_0053	Pantograph failure	2024-09-07	22:00:00	Inspection	20	Nil	Hardware	Yes		Nil		2024-09-07	22:10:00	2024-09-07	22:30:00		Asset 50	\N	\N	\N	388	10	0	Ashik	Operator	Up	Pantograph	10000	TS#07	1987	0	Yes	TC	Yes	Yes
28802	RST/07-2025/FID_0054	Door failure	2024-09-08	22:00:00	Inspection	20	Nil	Hardware	Yes		Nil		2024-09-08	22:10:00	2024-09-08	22:30:00		Asset 52	\N	\N	\N	402	10	0	Ashik	Operator	Up	Emergency Door	10000	TS#09	1988	0	Yes	DMA	Yes	Yes
28772	RST/07-2025/FID_0024	HVAC-01	2024-08-29	11:30:00	Inspection	10	nil	Hardware	Yes		showing warnings 		2024-08-29	11:40:00	2024-08-29	11:50:00		Asset 33 	\N	\N	\N	420	10	0	mihir	Operator	Up	HVAC-01	80348	TS#21	1801	0	Yes	DMA, TC	Yes	Yes
28773	RST/07-2025/FID_0025	HVAC-02	2024-08-29	11:30:00	Inspection	10	nil	Hardware	Yes		Showing warnings 		2024-08-29	11:40:00	2024-08-29	11:50:00		Asset 35 	\N	\N	\N	419	10	0	mihir	Operator	Up	HVAC-02	80348	TS#21	1802	0	Yes	DMA, TC	Yes	Yes
28774	RST/07-2025/FID_0026	Announcements	2024-08-30	22:10:00	Inspection	10	nil	Hardware	Yes		Announcements happening in Auto Mode 		2024-08-30	22:20:00	2024-08-30	22:30:00		Asset 11 	\N	\N	\N	415	10	0	mihir	Maintainer	Up	Announcements	25000	TS#24	1790	0	Yes	DMA	Yes	Yes
28775	RST/07-2025/FID_0027	PA/PIS	2024-08-30	22:10:00	Inspection	10	nil	Hardware	Yes		PA/PIS data downloading\n		2024-08-30	22:20:00	2024-08-30	22:30:00		Asset 29 	\N	\N	\N	433	10	0	mihir	Maintainer	Up	PA/PIS	25000	TS#10	1799	0	Yes	DMA	Yes	Yes
28776	RST/07-2025/FID_0028	PA/PIS	2024-08-30	22:10:00	Inspection	10	nil 	Software	Yes		PA/PIS data downloading\n		2024-08-30	22:20:00	2024-08-30	22:30:00		Asset 37 	\N	\N	\N	433	10	0	mihir	Maintainer	Up	PA/PIS	25000	TS#24	1803	0	Yes	DMA	Yes	Yes
28777	RST/07-2025/FID_0029	MDS/CCTV	2024-08-13	22:30:00	Inspection	10	nil	Software	Yes		lost all cameras 		2024-08-13	22:40:00	2024-08-13	22:50:00		Asset 39 	\N	\N	\N	428	10	0	mihir	Maintainer	Up	MDS/CCTV	25000	TS#26	1804	0	Yes	DMA	Yes	Yes
28779	RST/07-2025/FID_0031	HVAC Unit -1	2024-08-13	22:30:00	Inspection	10	nil	Hardware	Yes		showing warning on TCMS		2024-08-13	22:40:00	2024-08-13	22:50:00		Asset 43 	\N	\N	\N	420	10	0	mihir	Operator	Up	HVAC Unit -1	25000	TS#16	1806	0	Yes	TC	Yes	Yes
28780	RST/07-2025/FID_0032	TCMS	2024-08-13	22:30:00	Inspection	10	nil	Hardware	Yes		TCMS Data download 		2024-08-13	22:40:00	2024-08-13	22:50:00		Asset 45	\N	\N	\N	395	10	0	mihir	Maintainer	Up	TCMS	0	TS#24	1807	0	Yes	DMA	Yes	Yes
28782	RST/07-2025/FID_0034	Saloon Door 	2024-08-13	22:30:00	Inspection	10	nil	Hardware	Yes		Door not open in 		2024-08-13	22:40:00	2024-08-13	22:50:00		Asset 49	\N	\N	\N	407	10	0	mihir	Maintainer	Up	Saloon Door 	0	TS#25	1810	0	Yes	DMA	Yes	Yes
28783	RST/07-2025/FID_0035	Saloon Door 	2024-08-12	22:10:00	Inspection	10	nil	Hardware	Yes		Abnormal sound from under frame 		2024-08-12	22:20:00	2024-08-12	22:30:00		Asset 15 	\N	\N	\N	407	10	0	mihir	Maintainer	Up	Saloon Door 	25000	TS#09	1792	0	Yes	TC	Yes	Yes
28784	RST/07-2025/FID_0036	HVAC Failure	2024-08-21	23:50:00	Inspection	20	Nil	Hardware	Yes		Replacement		2024-08-21	23:50:00	2024-08-22	00:10:00		Asset-2	192	\N	\N	421	10	0	Ashik	Operator	Up	HVAC	142935	TS#05	1808	0	Yes	TC	Yes	Yes
28786	RST/07-2025/FID_0038	BECU Failure	2024-08-25	14:00:00	Inspection	30	Nil	Hardware	Yes		Nil		2024-08-25	14:00:00	2024-08-25	14:30:00		Asset-6	\N	\N	\N	365	10	0	Ashik	Operator	Up	HVAC	125552	TS#03	1813	0	Yes	DMA	Yes	Yes
28787	RST/07-2025/FID_0039	CI Failure	2024-08-25	14:00:00	Inspection	30	Nil	Hardware	Yes		Nil		2024-08-25	14:00:00	2024-08-25	14:30:00		Asset-8	\N	\N	\N	412	10	0	Ashik	Operator	Up	HVAC	125552	TS#03	1815	0	Yes	DMA, TC, DMB	Yes	Yes
28788	RST/07-2025/FID_0040	BECU Failure	2024-08-25	14:50:00	Inspection	25	Nil	Hardware	Yes		Nil		2024-08-25	14:50:00	2024-08-25	15:15:00		Asset-14	\N	\N	\N	365	10	0	Ashik	Operator	Up	HVAC	126730	TS#02	1959	0	Yes	DMB	Yes	Yes
28789	RST/07-2025/FID_0041	MDS Failure	2024-08-25	15:00:00	Inspection	20	Nil	Hardware	Yes		Nil		2024-08-25	15:10:00	2024-08-25	15:30:00		Asset-16	\N	\N	\N	429	10	0	Ashik	Operator	Up	MDS	83106	TS#12	1962	0	Yes	DMB	Yes	Yes
28800	RST/07-2025/FID_0052	HVAC failure	2024-09-07	22:00:00	Inspection	20	Nil	Hardware	Yes		Nil		2024-09-07	22:10:00	2024-09-07	22:30:00		Asset 48	192	\N	\N	421	10	0	Ashik	Operator	Up	HVAC	10000	TS#24	1986	0	Yes	DMA, TC, DMB	Yes	Yes
28791	RST/07-2025/FID_0043	Wiper Failure	2024-08-25	15:25:00	Inspection	30	Nil	Hardware	Yes		Nil		2024-08-25	15:30:00	2024-08-25	16:00:00		Asset-20	\N	\N	\N	424	10	0	Ashik	Operator	Up	Wiper	97683	TS#14	1964	0	Yes	DMB	Yes	Yes
28792	RST/07-2025/FID_0044	BECU Failure	2024-08-25	07:11:00	Inspection	15	Nil	Hardware	Yes		Nil		2024-08-25	07:15:00	2024-08-25	07:30:00		Asset-22	\N	\N	\N	365	10	0	Ashik	Operator	Up	BECU	59392	TS#20	1965	0	Yes	DMB	Yes	Yes
28793	RST/07-2025/FID_0045	FDU Failure	2024-08-25	07:11:00	Inspection	15	Nil	Hardware	Yes		Nil		2024-08-25	07:15:00	2024-08-25	07:30:00		Asset-24	\N	\N	\N	426	10	0	Ashik	Operator	Up	FDU	59392	TS#20	1966	0	Yes	DMA, TC, DMB	Yes	Yes
28794	RST/07-2025/FID_0046	Door failure	2024-08-25	12:16:00	Inspection	15	Nil	Hardware	Yes		Nil		2024-08-25	12:30:00	2024-08-25	12:45:00		Asset-26	\N	\N	\N	403	10	0	Ashik	Operator	Up	Cab Door	9000	TS#28	1967	0	Yes	DMB	Yes	Yes
28799	RST/07-2025/FID_0051	HVAC failure	2024-09-06	10:00:00	Inspection	30	Nil	Hardware	Yes		Nil		2024-09-06	10:00:00	2024-09-06	10:30:00		Asset 46	194	\N	\N	421	10	0	Ashik	Operator	Up	HVAC	10000	TS#04	1985	0	Yes	DMA	Yes	Yes
28797	RST/07-2025/FID_0049	Door failure	2024-09-06	10:00:00	Inspection	30	Nil	Hardware	Yes		Nil		2024-09-06	10:00:00	2024-09-06	10:30:00		Asset 40	\N	\N	\N	406	10	0	Ashik	Operator	Up	Car Door	15000	TS#25	1977	0	Yes	DMA, TC, DMB	Yes	Yes
28798	RST/07-2025/FID_0050	HVAC failure	2024-09-06	10:00:00	Inspection	30	Nil	Hardware	Yes		Nil		2024-09-06	10:00:00	2024-09-06	10:30:00		Asset 42	\N	\N	\N	419	10	0	Ashik	Operator	Up	HVAC	10000	TS#23	1978	0	Yes	DMB	Yes	Yes
28790	RST/07-2025/FID_0042	HVAC Failure	2024-08-25	15:25:00	Inspection	30	Nil	Hardware	Yes		Nil		2024-08-25	15:30:00	2024-08-25	16:00:00		Asset-18	192	\N	\N	421	10	0	Ashik	Operator	Up	HVAC	97683	TS#14	1963	0	Yes	DMA, DMB	Yes	Yes
28785	RST/07-2025/FID_0037	HVAC Failure	2024-08-25	14:00:00	Inspection	30	Nil	Hardware	Yes		Nil		2024-08-25	14:00:00	2024-08-25	14:30:00		Asset-4	193	\N	\N	421	10	0	Ashik	Operator	Up	HVAC	125552	TS#03	1812	0	Yes	DMA	Yes	Yes
28795	RST/07-2025/FID_0047	CCTV failure	2024-08-25	08:10:00	Inspection	15	Nil	Hardware	Yes		Nil		2024-08-25	08:15:00	2024-08-25	08:30:00		Asset-28	\N	\N	2072	385	10	0	Ashik	Operator	Up	CCTV	0	TS#25	1968	0	Yes	DMB	Yes	Yes
28803	RST/07-2025/FID_0055	VCC failure	2024-09-08	22:00:00	Inspection	20	Nil	Hardware	Yes		Nil		2024-09-08	22:10:00	2024-09-08	22:30:00		Asset 54	\N	\N	\N	392	10	0	Ashik	Operator	Up	VCC	15000	TS#24	1989	0	Yes	DMB	Yes	Yes
28767	RST/07-2025/FID_0019	CI-2	2024-08-15	22:30:00	Inspection	10	nil	Random	Yes		TCMS Data Download 		2024-08-15	22:40:00	2024-08-15	22:50:00		Asset 5	189	\N	\N	414	10	0	mihir	Operator	Up	CI-2	25000	TS#26	1787	0	Yes	DMA	Yes	Yes
28768	RST/07-2025/FID_0020	CI-2	2024-08-15	22:30:00	Inspection	10	nil 	Software	Yes		TCMS Data Download 		2024-08-15	22:40:00	2024-08-15	22:50:00		Asset 7 	189	\N	\N	414	10	0	mihir	Operator	Up	CI-2	25000	TS#22	1788	0	Yes	DMA	Yes	Yes
28769	RST/07-2025/FID_0021	CI-2	2024-08-15	22:30:00	Inspection	10	nil	Software	Yes		TCMS Data Download 		2024-08-15	22:40:00	2024-08-15	22:50:00		Asset 9 	189	\N	\N	414	10	0	mihir	Operator	Up	CI-2	25000	TS#16	1789	0	Yes	DMA	Yes	Yes
28778	RST/07-2025/FID_0030	CI-2	2024-08-13	22:30:00	Inspection	10	nil	Software	Yes		CI-2 showing warning 		2025-08-13	22:40:00	2024-08-13	22:50:00		Asset 41 	189	\N	\N	414	10	0	mihir	Maintainer	Up	CI-2	25000	TS#08	1805	0	Yes	DMA	Yes	Yes
28796	RST/07-2025/FID_0048	Door failure	2024-08-05	10:40:00	Inspection	30	Nil	Hardware	Yes		Nil		2024-08-05	10:50:00	2024-08-05	11:20:00		Asset 38	\N	\N	\N	406	10	0	Ashik	Operator	Up	Car Door	15000	TS#26	1973	0	Yes	DMA, TC, DMB	Yes	Yes
28804	RST/07-2025/FID_0056	PCU failure	2024-09-10	09:13:00	Inspection	15	Nil	Hardware	Yes		Nil		2024-09-10	09:15:00	2024-09-10	09:30:00		Asset 56	\N	\N	\N	433	10	0	Ashik	Operator	Up	PA/PIS	15000	TS#21	1990	0	Yes	DMA	Yes	Yes
28805	RST/07-2025/FID_0057	HVAC Failure	2025-07-29	14:36:00	Inspection	11	Part has been removed	Hardware	Yes		HVAC maintenance is been done. 		2025-07-29	14:39:00	2025-07-29	14:50:00		Asset 48	190	\N	\N	421	10	0	Ashik	Operator	Up	HVAC	12000	TS#25	1986	0	Yes	DMA, DMB	Yes	Yes
28765	RST/07-2025/FID_0017	CI-2 Component failure	2024-08-15	22:30:00	Inspection	10	Nil	Hardware	Yes		TCMS Data downloaded		2024-08-15	22:40:00	2024-08-15	22:50:00		Asset-1	189	\N	\N	414	10	0	Ashik	Maintainer	Up	CI-2	160000	TS#21	1785	0	Yes	DMA	Yes	Yes
28806	RST/07-2025/FID_0058	HVAC Failure	2025-07-31	15:31:00	Inspection	15	Troubleshot removed	Hardware	No		Removed dirt from the fan 		2025-07-31	15:45:00	2025-07-31	16:00:00		Asset-2	194	\N	\N	421	10	0	Mahtab	Operator	Up	HVAC	132656	IBL 1 	1808	0	Yes	DMA	Yes	No
\.


--
-- Data for Name: fracas_failuredataids; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_failuredataids (uid_id, year, month, last_id) FROM stdin;
1	2025	6	2
2	2025	7	58
\.


--
-- Data for Name: fracas_failuremode; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_failuremode (id, mode_id, asset_type, end_date, start_date, mode_description, "P_id", is_active) FROM stdin;
2071	HJJJ	{414}	2024-09-04	2024-08-02	RTRTTT	10	1
2072	01	{385}	2024-08-30	2024-08-07	rt	10	0
\.


--
-- Data for Name: fracas_history; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_history (id, "P_id", date, message, "time", user_id, function_name) FROM stdin;
963	0	2025-06-23	Login	07:01:54	14	Manage Users
964	0	2025-06-23	Login	07:45:11	14	Manage Users
965	0	2025-06-23	Login	08:06:21	14	Manage Users
966	0	2025-06-23	Login	08:12:59	14	Manage Users
967	0	2025-06-23	ID: 1771=> Add new Asset  	08:15:47	14	Asset Register
968	0	2025-06-23	ID: 28745=> Add new failure data 	08:40:38	14	Failure Data Collection
969	0	2025-06-23	ID: 1772=> Add new Asset  	10:36:32	14	Asset Register
970	0	2025-06-23	ID: 28746=> Add new failure data 	10:41:55	14	Failure Data Collection
971	0	2025-06-25	Logout	07:54:47	14	Manage Users
972	0	2025-06-25	Login	07:55:00	14	Manage Users
973	0	2025-06-25	ID: 28745=> mode_id_id: None to , incident: No to Yes, 	15:23:03	14	Failure Data Collection
974	0	2025-06-25	ID: 28746=> mode_id_id: None to , incident: No to Yes, 	15:23:39	14	Failure Data Collection
975	0	2025-06-25	ID: 28747=> Add new failure data 	15:30:19	14	Failure Data Collection
976	0	2025-06-26	Login	11:05:04	14	Manage Users
977	0	2025-06-26	Logout	11:09:54	14	Manage Users
978	0	2025-06-26	Login	11:14:38	14	Manage Users
979	0	2025-06-26	ID: 28746=> asset_type: Saloon Door to 3E Camera, asset_config_id_id: Asset_2 to Asset_1, mode_id_id: None to , location_id: 1772 to 1771, 	11:17:13	14	Failure Data Collection
980	0	2025-06-26	Login	12:01:54	14	Manage Users
981	0	2025-06-27	Login	12:26:58	14	Manage Users
982	0	2025-06-27	ID: 28748=> Add new failure data 	12:36:52	14	Failure Data Collection
983	0	2025-06-28	Login	11:31:38	14	Manage Users
984	0	2025-07-02	Login	10:44:11	14	Manage Users
985	0	2025-07-02	ID: 349=> Delete PBSMaster	11:13:35	14	PBS Master
986	0	2025-07-02	ID: 350=> Delete PBSMaster	11:13:41	14	PBS Master
987	0	2025-07-02	ID: 351=> Delete PBSMaster	11:13:46	14	PBS Master
988	0	2025-07-02	ID: 353=> Delete PBSMaster	11:13:55	14	PBS Master
989	0	2025-07-02	ID: 354=> Delete PBSMaster	11:13:59	14	PBS Master
990	0	2025-07-02	ID: 355=> Delete PBSMaster	11:14:04	14	PBS Master
991	0	2025-07-02	ID: 356=> Delete PBSMaster	11:14:08	14	PBS Master
992	0	2025-07-02	ID: 357=> Delete PBSMaster	11:14:13	14	PBS Master
993	0	2025-07-02	ID: 358=> Delete PBSMaster	11:14:19	14	PBS Master
994	0	2025-07-02	ID: 359=> Delete PBSMaster	11:14:24	14	PBS Master
995	0	2025-07-02	ID: 360=> Delete PBSMaster	11:14:38	14	PBS Master
996	0	2025-07-02	ID: 361=> Delete PBSMaster	11:14:45	14	PBS Master
997	0	2025-07-02	ID: 362=> Delete PBSMaster	11:14:54	14	PBS Master
998	0	2025-07-02	ID: 363=> Delete PBSMaster	11:15:01	14	PBS Master
999	0	2025-07-02	ID: 1771=> Delete asset 	11:22:52	14	Asset Register
1000	0	2025-07-02	ID: 1773=> Add new Asset  	11:46:35	14	Asset Register
1001	0	2025-07-02	ID: 1772=> Delete asset 	11:46:51	14	Asset Register
1002	0	2025-07-02	ID: 1774=> Add new Asset  	11:49:10	14	Asset Register
1003	0	2025-07-02	ID: 1774=> asset_serial_number: HVAC_01 to HVAC-01, 	11:49:30	14	Asset Register
1004	0	2025-07-02	ID: 1775=> Add new Asset  	11:51:10	14	Asset Register
1005	0	2025-07-02	ID: 1776=> Add new Asset  	11:52:35	14	Asset Register
1006	0	2025-07-02	ID: 1777=> Add new Asset  	11:53:15	14	Asset Register
1007	0	2025-07-02	ID: 1778=> Add new Asset  	11:53:47	14	Asset Register
1008	0	2025-07-02	ID: 1779=> Add new Asset  	11:54:41	14	Asset Register
1009	0	2025-07-02	ID: 1780=> Add new Asset  	12:02:05	14	Asset Register
1010	0	2025-07-02	ID: 1781=> Add new Asset  	12:02:44	14	Asset Register
1011	0	2025-07-02	ID: 1782=> Add new Asset  	12:03:42	14	Asset Register
1012	0	2025-07-02	ID: 1783=> Add new Asset  	12:05:07	14	Asset Register
1013	0	2025-07-02	ID: 1784=> Add new Asset  	12:06:40	14	Asset Register
1014	0	2025-07-02	ID: 1773=> asset_config_id: Asset-1 to Asset-01, 	12:08:33	14	Asset Register
1015	0	2025-07-02	ID: 1774=> asset_config_id: Asset-2 to Asset-02, 	12:08:50	14	Asset Register
1016	0	2025-07-02	ID: 1775=> asset_config_id: Asset-3 to Asset-03, 	12:09:00	14	Asset Register
1017	0	2025-07-02	ID: 1776=> asset_config_id: Asset-4 to Asset-04, 	12:09:16	14	Asset Register
1018	0	2025-07-02	ID: 1777=> asset_config_id: Asset-5 to Asset-05, 	12:09:34	14	Asset Register
1019	0	2025-07-02	ID: 1778=> asset_config_id: Asset-6 to Asset-06, 	12:09:45	14	Asset Register
1020	0	2025-07-02	ID: 1779=> asset_config_id: Asset-7 to Asset-07, 	12:09:56	14	Asset Register
1021	0	2025-07-02	ID: 1780=> asset_config_id: Asset-8 to Asset-08, 	12:10:12	14	Asset Register
1022	0	2025-07-02	ID: 1781=> asset_config_id: Asset-9 to Asset-09, 	12:10:28	14	Asset Register
1023	0	2025-07-02	ID: 28749=> Add new failure data 	14:15:18	14	Failure Data Collection
1024	0	2025-07-02	ID: 28750=> Add new failure data 	14:26:24	14	Failure Data Collection
1025	0	2025-07-02	ID: 28751=> Add new failure data 	14:47:27	14	Failure Data Collection
1026	0	2025-07-02	ID: 28752=> Add new failure data 	14:54:38	14	Failure Data Collection
1027	0	2025-07-02	ID: 28753=> Add new failure data 	15:47:27	14	Failure Data Collection
1028	0	2025-07-02	ID: 28754=> Add new failure data 	15:55:40	14	Failure Data Collection
1029	0	2025-07-02	ID: 28755=> Add new failure data 	15:58:24	14	Failure Data Collection
1030	0	2025-07-02	ID: 28756=> Add new failure data 	16:00:03	14	Failure Data Collection
1031	0	2025-07-02	ID: 28757=> Add new failure data 	16:01:49	14	Failure Data Collection
1032	0	2025-07-02	ID: 28758=> Add new failure data 	16:03:06	14	Failure Data Collection
1033	0	2025-07-02	ID: 28759=> Add new failure data 	16:08:16	14	Failure Data Collection
1034	0	2025-07-02	ID: 28760=> Add new failure data 	16:09:39	14	Failure Data Collection
1035	0	2025-07-02	ID: 28761=> Add new failure data 	16:22:54	14	Failure Data Collection
1036	0	2025-07-03	Login	10:31:30	14	Manage Users
1037	0	2025-07-03	Logout	10:53:02	14	Manage Users
1038	0	2025-07-03	Login	10:53:20	14	Manage Users
1039	0	2025-07-03	USERNAME: operator@gmail.com=> Add new user 	11:33:57	14	Manage Users
1040	0	2025-07-03	USERNAME: maintainer@gmail.com=> Add new user 	11:35:37	14	Manage Users
1041	0	2025-07-03	USERNAME: ram@gmail.com=> Add new user 	11:37:52	14	Manage Users
1042	0	2025-07-03	USERNAME: adminlevel@gmail.com=> Add new user 	11:39:41	14	Manage Users
1043	0	2025-07-03	USERNAME: viewlevel@gmail.com=> Add new user 	11:40:05	14	Manage Users
1044	0	2025-07-03	Logout	12:38:11	14	Manage Users
1045	10	2025-07-03	Login	12:38:32	25	Manage Users
1046	10	2025-07-03	Logout	16:19:14	25	Manage Users
1047	10	2025-07-03	Login	16:19:28	26	Manage Users
1048	10	2025-07-03	Logout	17:58:59	26	Manage Users
1049	10	2025-07-03	Login	17:59:16	27	Manage Users
1050	10	2025-07-03	Logout	18:00:17	27	Manage Users
1051	10	2025-07-03	Login	18:00:28	25	Manage Users
1052	10	2025-07-03	Logout	18:19:00	25	Manage Users
1053	10	2025-07-03	Login	18:19:12	27	Manage Users
1054	0	2025-07-04	Login	03:12:11	14	Manage Users
1055	10	2025-07-04	Login	09:37:00	25	Manage Users
1056	10	2025-07-04	Logout	09:41:58	25	Manage Users
1057	10	2025-07-04	Login	09:42:29	27	Manage Users
1058	10	2025-07-04	ID: 28762=> Add new failure data 	09:47:54	27	Failure Data Collection
1059	10	2025-07-04	Logout	09:50:05	27	Manage Users
1060	10	2025-07-04	Login	09:50:15	25	Manage Users
1061	0	2025-07-04	Logout	10:02:18	14	Manage Users
1062	10	2025-07-04	Login	10:02:37	25	Manage Users
1063	10	2025-07-04	Logout	10:03:12	25	Manage Users
1064	10	2025-07-04	Login	10:03:41	27	Manage Users
1065	10	2025-07-04	Logout	10:05:19	27	Manage Users
1066	10	2025-07-04	Login	10:05:30	25	Manage Users
1067	10	2025-07-04	Logout	10:06:07	25	Manage Users
1068	10	2025-07-04	Login	10:06:21	26	Manage Users
1069	10	2025-07-04	Logout	10:06:45	26	Manage Users
1070	10	2025-07-04	Login	10:06:50	25	Manage Users
1071	10	2025-07-04	Logout	10:08:32	25	Manage Users
1072	0	2025-07-04	Login	10:08:39	14	Manage Users
1073	0	2025-07-04	Logout	10:24:21	14	Manage Users
1074	10	2025-07-04	Login	10:24:34	26	Manage Users
1075	10	2025-07-04	Logout	10:24:45	26	Manage Users
1076	10	2025-07-04	Login	10:24:51	27	Manage Users
1077	10	2025-07-04	Logout	10:25:03	27	Manage Users
1078	0	2025-07-04	Login	10:25:10	14	Manage Users
1079	0	2025-07-04	Logout	10:25:19	14	Manage Users
1080	10	2025-07-04	Login	10:25:25	25	Manage Users
1081	10	2025-07-04	Logout	10:30:53	25	Manage Users
1082	10	2025-07-04	Login	10:30:58	26	Manage Users
1083	10	2025-07-04	Logout	10:31:13	26	Manage Users
1084	10	2025-07-04	Login	10:31:28	25	Manage Users
1085	10	2025-07-04	Logout	10:34:21	25	Manage Users
1086	10	2025-07-04	Login	10:34:53	27	Manage Users
1087	10	2025-07-04	Logout	10:37:56	27	Manage Users
1088	10	2025-07-04	Login	10:38:07	25	Manage Users
1089	10	2025-07-04	Logout	10:39:03	25	Manage Users
1090	10	2025-07-04	Login	10:39:23	27	Manage Users
1091	10	2025-07-04	ID: 28763=> Add new failure data 	11:11:54	27	Failure Data Collection
1092	10	2025-07-04	Logout	11:12:32	27	Manage Users
1093	10	2025-07-04	Login	11:12:45	25	Manage Users
1094	10	2025-07-04	Logout	11:13:43	25	Manage Users
1095	10	2025-07-04	Login	11:13:55	25	Manage Users
1096	10	2025-07-04	Logout	11:15:44	25	Manage Users
1097	10	2025-07-04	Login	11:15:55	26	Manage Users
1098	10	2025-07-04	Logout	11:20:40	26	Manage Users
1099	10	2025-07-04	Login	11:20:48	25	Manage Users
1100	10	2025-07-04	Logout	11:29:57	25	Manage Users
1101	10	2025-07-04	Login	11:30:08	27	Manage Users
1102	10	2025-07-04	ID: 28764=> Add new failure data 	11:35:05	27	Failure Data Collection
1103	10	2025-07-04	Logout	11:35:20	27	Manage Users
1104	10	2025-07-04	Login	11:35:32	25	Manage Users
1105	10	2025-07-04	Logout	11:38:59	25	Manage Users
1106	10	2025-07-04	Login	11:39:08	26	Manage Users
1107	10	2025-07-04	Logout	11:41:59	26	Manage Users
1108	10	2025-07-04	Login	11:42:09	25	Manage Users
1109	10	2025-07-04	Logout	13:02:20	25	Manage Users
1110	0	2025-07-04	Login	13:02:38	14	Manage Users
1111	0	2025-07-04	ID: 28750=> mode_id_id: None to , cm_end_time: 15:00:00 to 17:00, 	14:37:34	14	Failure Data Collection
1112	0	2025-07-04	ID: 28751=> mode_id_id: None to , cm_end_time: 15:00:00 to 17:00, 	14:38:07	14	Failure Data Collection
1113	0	2025-07-04	ID: 28752=> mode_id_id: None to , cm_end_time: 15:00:00 to 17:00, 	14:38:31	14	Failure Data Collection
1114	0	2025-07-05	ID: 364 => asset_quantity: 34 to 4, 	13:19:46	14	PBS Master
1115	0	2025-07-05	ID: 365 => asset_quantity: 34 to 2, 	13:20:17	14	PBS Master
1116	10	2025-07-07	Logout	09:32:12	25	Manage Users
1117	0	2025-07-07	Login	09:34:43	14	Manage Users
1118	0	2025-07-07	ID: [28749, 28750, 28751, 28752, 28753, 28754, 28755, 28756, 28757, 28758]=> Delete failuredatas 	09:41:21	14	Failure Data Collection
1119	0	2025-07-07	ID: [28759, 28760, 28761, 28762, 28763, 28764]=> Delete failuredatas 	09:41:30	14	Failure Data Collection
1120	0	2025-07-07	ID: [28759, 28760, 28761, 28762, 28763, 28764]=> Delete failuredatas 	09:41:31	14	Failure Data Collection
1121	0	2025-07-07	ID: [1773, 1774, 1775, 1776, 1777, 1778, 1779, 1780, 1781, 1782]=> Delete assets 	09:54:00	14	Asset Register
1122	0	2025-07-07	ID: [1783, 1784]=> Delete assets 	09:54:10	14	Asset Register
1123	0	2025-07-07	ID: 1785=> Add new Asset  	11:00:14	14	Asset Register
1124	0	2025-07-07	ID: 1786=> Add new Asset  	11:03:18	14	Asset Register
1125	0	2025-07-07	ID: 1787=> Add new Asset  	11:05:39	14	Asset Register
1126	0	2025-07-07	ID: 1788=> Add new Asset  	11:06:44	14	Asset Register
1127	0	2025-07-07	ID: 1789=> Add new Asset  	11:07:45	14	Asset Register
1128	0	2025-07-07	ID: 1790=> Add new Asset  	11:11:36	14	Asset Register
1129	0	2025-07-07	ID: 1791=> Add new Asset  	11:16:20	14	Asset Register
1130	0	2025-07-07	ID: 1792=> Add new Asset  	11:18:30	14	Asset Register
1131	0	2025-07-07	ID: 1793=> Add new Asset  	11:20:52	14	Asset Register
1132	0	2025-07-07	ID: 1794=> Add new Asset  	11:23:49	14	Asset Register
1133	0	2025-07-07	ID: 1795=> Add new Asset  	11:24:59	14	Asset Register
1134	0	2025-07-07	ID: 1796=> Add new Asset  	11:30:04	14	Asset Register
1135	0	2025-07-07	ID: 1797=> Add new Asset  	11:31:19	14	Asset Register
1136	0	2025-07-07	ID: 1798=> Add new Asset  	11:45:28	14	Asset Register
1137	0	2025-07-07	ID: 1799=> Add new Asset  	11:49:29	14	Asset Register
1138	0	2025-07-07	ID: 1800=> Add new Asset  	11:51:38	14	Asset Register
1139	0	2025-07-07	ID: 1801=> Add new Asset  	11:53:41	14	Asset Register
1140	0	2025-07-07	ID: 1802=> Add new Asset  	11:54:24	14	Asset Register
1141	0	2025-07-07	ID: 1803=> Add new Asset  	11:56:59	14	Asset Register
1142	0	2025-07-07	ID: 1804=> Add new Asset  	11:58:03	14	Asset Register
1143	0	2025-07-07	ID: 1805=> Add new Asset  	11:59:58	14	Asset Register
1144	0	2025-07-07	ID: 1806=> Add new Asset  	12:02:02	14	Asset Register
1145	0	2025-07-07	ID: 1807=> Add new Asset  	12:03:43	14	Asset Register
1146	0	2025-07-07	ID: 1808=> Add new Asset  	12:04:52	14	Asset Register
1147	0	2025-07-07	ID: 1809=> Add new Asset  	12:05:09	14	Asset Register
1148	0	2025-07-07	ID: 1810=> Add new Asset  	12:06:50	14	Asset Register
1149	0	2025-07-07	ID: 1811=> Add new Asset  	12:08:37	14	Asset Register
1150	0	2025-07-07	ID: 1812=> Add new Asset  	12:08:46	14	Asset Register
1151	0	2025-07-07	ID: 1813=> Add new Asset  	12:10:08	14	Asset Register
1152	0	2025-07-07	ID: 1814=> Add new Asset  	12:10:33	14	Asset Register
1153	0	2025-07-07	ID: 1815=> Add new Asset  	12:12:44	14	Asset Register
1154	0	2025-07-07	ID: 1816=> Add new Asset  	12:13:47	14	Asset Register
1155	0	2025-07-07	ID: 1817=> Add new Asset  	12:15:14	14	Asset Register
1156	0	2025-07-07	ID: 1818=> Add new Asset  	12:17:14	14	Asset Register
1157	0	2025-07-07	ID: 1829=> Add new Asset  	12:20:03	14	Asset Register
1158	0	2025-07-07	ID: 1830=> Add new Asset  	12:21:43	14	Asset Register
1159	0	2025-07-07	ID: 1831=> Add new Asset  	12:24:05	14	Asset Register
1160	0	2025-07-07	ID: 1855=> Add new Asset  	12:28:44	14	Asset Register
1161	0	2025-07-07	ID: 1856=> Add new Asset  	12:29:18	14	Asset Register
1162	0	2025-07-07	ID: 1857=> Add new Asset  	12:30:02	14	Asset Register
1163	0	2025-07-07	ID: 1858=> Add new Asset  	12:30:40	14	Asset Register
1164	0	2025-07-07	ID: 1856=> asset_status: UNDER MAINTENANCE to ACTIVE, 	12:31:21	14	Asset Register
1165	0	2025-07-07	ID: 1864=> Add new Asset  	12:38:27	14	Asset Register
1166	0	2025-07-07	ID: 1865=> Add new Asset  	12:40:18	14	Asset Register
1167	0	2025-07-07	ID: 1866=> Add new Asset  	12:43:50	14	Asset Register
1168	0	2025-07-07	ID: 1867=> Add new Asset  	12:46:41	14	Asset Register
1169	0	2025-07-07	ID: 1868=> Add new Asset  	12:49:12	14	Asset Register
1170	0	2025-07-07	Logout	14:46:58	14	Manage Users
1171	0	2025-07-07	Login	14:47:10	14	Manage Users
1172	0	2025-07-07	Login	14:49:17	14	Manage Users
1173	0	2025-07-07	ID: 1959=> Add new Asset  	15:35:50	14	Asset Register
1174	0	2025-07-07	ID: 1867=> asset_config_id: Asst 81  to Asset 81 , 	15:36:56	14	Asset Register
1175	0	2025-07-07	ID: 1960=> Add new Asset  	15:41:22	14	Asset Register
1176	0	2025-07-07	ID: 1960=> Delete asset 	15:41:49	14	Asset Register
1177	0	2025-07-07	ID: 1961=> Add new Asset  	15:42:17	14	Asset Register
1178	0	2025-07-07	ID: 1961=> Delete asset 	15:43:22	14	Asset Register
1179	0	2025-07-07	ID: 1962=> Add new Asset  	16:58:16	14	Asset Register
1180	0	2025-07-07	ID: 1963=> Add new Asset  	17:00:01	14	Asset Register
1181	0	2025-07-07	ID: 1964=> Add new Asset  	17:02:12	14	Asset Register
1182	0	2025-07-07	ID: 1965=> Add new Asset  	17:05:50	14	Asset Register
1183	0	2025-07-07	ID: 1966=> Add new Asset  	17:07:36	14	Asset Register
1184	0	2025-07-07	ID: 1966=> location_id: TS#24 to TS#20, location_description: TS#24 to TS#20, sub_location: TS#24 to TS#20, 	17:11:35	14	Asset Register
1185	0	2025-07-07	ID: 1967=> Add new Asset  	17:13:59	14	Asset Register
1186	0	2025-07-07	ID: 1968=> Add new Asset  	17:16:09	14	Asset Register
1187	0	2025-07-07	ID: 1969=> Add new Asset  	17:39:14	14	Asset Register
1188	0	2025-07-07	ID: 1970=> Add new Asset  	18:07:14	14	Asset Register
1189	0	2025-07-07	ID: 1971=> Add new Asset  	18:23:00	14	Asset Register
1190	0	2025-07-07	ID: 1972=> Add new Asset  	18:30:23	14	Asset Register
1191	0	2025-07-08	ID: 28765=> Add new failure data 	10:41:46	14	Failure Data Collection
1192	0	2025-07-08	ID: 28766=> Add new failure data 	10:54:12	14	Failure Data Collection
1193	0	2025-07-08	ID: 28767=> Add new failure data 	10:56:35	14	Failure Data Collection
1194	0	2025-07-08	ID: 28768=> Add new failure data 	10:59:13	14	Failure Data Collection
1195	0	2025-07-08	ID: 28769=> Add new failure data 	11:01:34	14	Failure Data Collection
1196	0	2025-07-08	ID: 28770=> Add new failure data 	11:09:36	14	Failure Data Collection
1197	0	2025-07-08	ID: 28771=> Add new failure data 	11:13:00	14	Failure Data Collection
1198	0	2025-07-08	ID: 28772=> Add new failure data 	11:16:08	14	Failure Data Collection
1199	0	2025-07-08	ID: 28773=> Add new failure data 	11:18:52	14	Failure Data Collection
1200	0	2025-07-08	ID: 28774=> Add new failure data 	11:22:20	14	Failure Data Collection
1201	0	2025-07-08	ID: 28775=> Add new failure data 	11:26:39	14	Failure Data Collection
1202	0	2025-07-08	ID: 28776=> Add new failure data 	11:29:29	14	Failure Data Collection
1203	0	2025-07-08	ID: 28777=> Add new failure data 	11:32:42	14	Failure Data Collection
1204	0	2025-07-08	ID: 28778=> Add new failure data 	11:35:56	14	Failure Data Collection
1205	0	2025-07-08	ID: 28779=> Add new failure data 	11:39:11	14	Failure Data Collection
1206	0	2025-07-08	ID: 28780=> Add new failure data 	11:42:13	14	Failure Data Collection
1207	0	2025-07-08	ID: 28780=> mode_id_id: None to , 	11:45:39	14	Failure Data Collection
1208	0	2025-07-08	ID: 28781=> Add new failure data 	11:48:49	14	Failure Data Collection
1209	0	2025-07-08	ID: 28782=> Add new failure data 	11:51:46	14	Failure Data Collection
1210	0	2025-07-08	ID: 28783=> Add new failure data 	11:54:54	14	Failure Data Collection
1211	0	2025-07-09	ID: 1973=> Add new Asset  	10:02:43	14	Asset Register
1212	0	2025-07-09	ID: 1974=> Add new Asset  	10:04:07	14	Asset Register
1213	0	2025-07-09	ID: 1975=> Add new Asset  	10:05:32	14	Asset Register
1214	0	2025-07-09	ID: 1976=> Add new Asset  	10:07:47	14	Asset Register
1215	0	2025-07-09	ID: 1977=> Add new Asset  	10:08:08	14	Asset Register
1216	0	2025-07-09	ID: 1978=> Add new Asset  	10:10:12	14	Asset Register
1217	0	2025-07-09	ID: 1978=> asset_serial_number: HVAC-23 to HVAC Unit 2-23, asset_type: HVAC to HVAC Unit-2, 	10:11:02	14	Asset Register
1218	0	2025-07-09	ID: 1979=> Add new Asset  	10:13:04	14	Asset Register
1219	0	2025-07-09	ID: 1980=> Add new Asset  	10:16:10	14	Asset Register
1220	0	2025-07-09	ID: 1981=> Add new Asset  	10:18:20	14	Asset Register
1221	0	2025-07-09	ID: 1982=> Add new Asset  	10:21:20	14	Asset Register
1222	0	2025-07-09	ID: 1983=> Add new Asset  	10:23:04	14	Asset Register
1223	0	2025-07-09	ID: 1984=> Add new Asset  	10:28:40	14	Asset Register
1224	0	2025-07-09	ID: 1985=> Add new Asset  	11:16:04	14	Asset Register
1225	0	2025-07-09	ID: 1986=> Add new Asset  	11:18:17	14	Asset Register
1226	0	2025-07-09	ID: 1987=> Add new Asset  	11:20:08	14	Asset Register
1227	0	2025-07-09	ID: 1988=> Add new Asset  	11:22:05	14	Asset Register
1228	0	2025-07-09	ID: 1989=> Add new Asset  	11:26:21	14	Asset Register
1229	0	2025-07-09	ID: 1990=> Add new Asset  	11:31:04	14	Asset Register
1230	0	2025-07-09	ID: 1991=> Add new Asset  	11:32:19	14	Asset Register
1231	0	2025-07-09	ID: 1984=> Delete asset 	11:55:08	14	Asset Register
1232	0	2025-07-09	ID: 1992=> Add new Asset  	12:00:03	14	Asset Register
1233	0	2025-07-09	ID: 1993=> Add new Asset  	12:01:12	14	Asset Register
1234	0	2025-07-09	ID: 28784=> Add new failure data 	14:11:49	14	Failure Data Collection
1235	0	2025-07-09	ID: 28785=> Add new failure data 	14:22:38	14	Failure Data Collection
1236	0	2025-07-09	ID: 28786=> Add new failure data 	14:25:16	14	Failure Data Collection
1237	0	2025-07-09	ID: 28787=> Add new failure data 	14:32:55	14	Failure Data Collection
1238	0	2025-07-09	ID: 28788=> Add new failure data 	15:12:24	14	Failure Data Collection
1239	0	2025-07-09	ID: 28789=> Add new failure data 	15:47:27	14	Failure Data Collection
1240	0	2025-07-09	ID: 28790=> Add new failure data 	15:52:25	14	Failure Data Collection
1241	0	2025-07-09	ID: 28791=> Add new failure data 	15:56:54	14	Failure Data Collection
1242	0	2025-07-09	ID: 28792=> Add new failure data 	15:59:48	14	Failure Data Collection
1243	0	2025-07-09	ID: 28793=> Add new failure data 	16:03:02	14	Failure Data Collection
1244	0	2025-07-09	ID: 28794=> Add new failure data 	16:06:12	14	Failure Data Collection
1245	0	2025-07-09	ID: 28795=> Add new failure data 	16:09:09	14	Failure Data Collection
1246	0	2025-07-09	ID: 28796=> Add new failure data 	16:22:26	14	Failure Data Collection
1247	0	2025-07-09	ID: 28797=> Add new failure data 	16:25:51	14	Failure Data Collection
1248	0	2025-07-09	ID: 28798=> Add new failure data 	16:28:52	14	Failure Data Collection
1249	0	2025-07-09	ID: 28799=> Add new failure data 	16:35:31	14	Failure Data Collection
1250	0	2025-07-09	ID: 28800=> Add new failure data 	16:37:24	14	Failure Data Collection
1251	0	2025-07-09	ID: 28801=> Add new failure data 	16:40:20	14	Failure Data Collection
1252	0	2025-07-09	ID: 28802=> Add new failure data 	16:42:33	14	Failure Data Collection
1253	0	2025-07-09	ID: 28803=> Add new failure data 	16:45:53	14	Failure Data Collection
1254	0	2025-07-09	ID: 28804=> Add new failure data 	16:48:33	14	Failure Data Collection
1255	0	2025-07-09	Login	17:07:09	14	Manage Users
1256	0	2025-07-09	Login	17:18:42	14	Manage Users
1257	0	2025-07-10	Login	09:36:10	14	Manage Users
1258	0	2025-07-14	Login	14:34:58	14	Manage Users
1259	0	2025-07-14	Login	15:03:37	14	Manage Users
1260	0	2025-07-14	Login	16:20:29	14	Manage Users
1261	0	2025-07-15	Login	09:41:04	14	Manage Users
1262	0	2025-07-15	Login	10:01:26	14	Manage Users
1263	0	2025-07-15	Login	10:02:25	14	Manage Users
1264	0	2025-07-15	Login	10:32:23	14	Manage Users
1265	0	2025-07-15	DEFECT ID: 189=> Add new defect 	10:38:59	14	FRACAS Defect Identification
1266	0	2025-07-15	DEFECT ID: 189=> defect_description:  to defect, investigation:  to investigation , defect_status_remarks:  to open, oem_defect_reference:  to oem defect, defect_status:  to Open, oem_target_date: None to 2025-07-24, defect_open_date: None to 2024-08-01, defect_closed_date: None to 2024-09-01, 	10:47:43	14	FRACAS Defect Identification
1267	0	2025-07-15	ID: 87=> Add new rootcause 	10:51:09	14	Root Cause Analysis
1268	0	2025-07-15	Login	11:55:34	14	Manage Users
1269	0	2025-07-15	Logout	16:17:32	14	Manage Users
1270	0	2025-07-15	Login	16:17:43	14	Manage Users
1271	0	2025-07-15	Logout	16:42:55	14	Manage Users
1272	10	2025-07-15	Login	16:43:25	25	Manage Users
1273	10	2025-07-15	Logout	17:16:53	25	Manage Users
1274	10	2025-07-15	Login	17:17:21	26	Manage Users
1275	10	2025-07-15	Logout	17:25:21	26	Manage Users
1276	10	2025-07-15	Login	17:25:27	25	Manage Users
1277	10	2025-07-15	Logout	17:38:16	25	Manage Users
1278	10	2025-07-15	Login	17:38:21	26	Manage Users
1279	10	2025-07-15	Logout	17:39:01	26	Manage Users
1280	10	2025-07-15	Login	17:40:35	27	Manage Users
1281	10	2025-07-16	Logout	12:34:26	27	Manage Users
1282	10	2025-07-16	Login	12:34:39	25	Manage Users
1283	0	2025-07-16	Login	12:38:24	14	Manage Users
1284	0	2025-07-16	ID: 1790 => asset_serial_number: Announcement - 24  to Announcement/TS#24/TC/001, sub_location: TS#24  to TC, 	12:38:53	14	Asset Register
1285	10	2025-07-16	Logout	12:42:57	25	Manage Users
1286	10	2025-07-16	Login	12:43:04	26	Manage Users
1287	10	2025-07-16	Logout	12:46:26	26	Manage Users
1288	10	2025-07-16	Login	12:46:36	27	Manage Users
1289	10	2025-07-16	Logout	12:53:14	27	Manage Users
1290	10	2025-07-16	Login	12:53:24	26	Manage Users
1291	10	2025-07-16	Logout	12:55:20	26	Manage Users
1292	10	2025-07-16	Login	12:55:25	27	Manage Users
1293	10	2025-07-16	Logout	14:17:29	27	Manage Users
1294	10	2025-07-16	Login	14:17:55	25	Manage Users
1295	10	2025-07-16	Logout	14:23:30	25	Manage Users
1296	0	2025-07-16	Login	14:23:36	14	Manage Users
1297	0	2025-07-16	Login	15:30:06	14	Manage Users
1298	0	2025-07-17	Login	10:55:52	14	Manage Users
1299	0	2025-07-17	DEFECT ID: 190=> Add new defect 	10:56:58	14	FRACAS Defect Identification
1300	0	2025-07-17	Logout	17:16:17	14	Manage Users
1301	10	2025-07-17	Login	17:16:25	26	Manage Users
1302	10	2025-07-17	Logout	17:16:40	26	Manage Users
1303	10	2025-07-17	Login	17:16:47	25	Manage Users
1304	10	2025-07-17	Logout	17:16:57	25	Manage Users
1305	0	2025-07-17	Login	17:17:03	14	Manage Users
1306	0	2025-07-17	ID: 82=> Add new review board	17:45:57	14	FRACAS Review Board
1307	0	2025-07-18	ID: 83=> Add new review board	10:20:34	14	FRACAS Review Board
1308	0	2025-07-18	ID: 83=> Delete review board	10:20:48	14	FRACAS Review Board
1309	0	2025-07-18	Logout	10:29:11	14	Manage Users
1310	10	2025-07-18	Login	10:29:34	26	Manage Users
1311	0	2025-07-18	Logout	12:09:06	14	Manage Users
1312	10	2025-07-18	Login	12:09:13	26	Manage Users
1313	10	2025-07-18	Logout	12:09:53	26	Manage Users
1314	0	2025-07-18	Login	12:10:03	14	Manage Users
1315	0	2025-07-18	Logout	12:11:30	14	Manage Users
1316	10	2025-07-18	Login	12:11:36	26	Manage Users
1317	10	2025-07-18	Logout	15:38:04	26	Manage Users
1318	0	2025-07-18	Login	15:38:12	14	Manage Users
1319	0	2025-07-19	PRODUCT ID: 10 => num_of_trains: 0 to 34, 	12:05:38	14	Add Project RAM Targets
1320	0	2025-07-22	Logout	12:01:50	14	Manage Users
1321	0	2025-07-22	Login	12:01:57	14	Manage Users
1322	0	2025-07-23	PRODUCT ID: 10 => MTBF: 700.0 to 2941, 	10:37:00	14	Add Project RAM Targets
1323	0	2025-07-23	PRODUCT ID: 10 => MTBF: 2941.0 to 2941.176, MTBSAF: 100000.0 to 2941.176, 	10:39:10	14	Add Project RAM Targets
1324	0	2025-07-23	Logout	15:09:39	14	Manage Users
1325	10	2025-07-23	Login	15:09:46	26	Manage Users
1326	0	2025-07-23	Login	16:29:54	14	Manage Users
1327	0	2025-07-23	Logout	16:42:32	14	Manage Users
1328	0	2025-07-23	Login	16:42:37	14	Manage Users
1329	0	2025-07-23	Logout	16:47:02	14	Manage Users
1330	0	2025-07-23	Login	16:47:11	14	Manage Users
1331	0	2025-07-23	Logout	16:57:41	14	Manage Users
1332	0	2025-07-23	Login	16:58:02	14	Manage Users
1333	0	2025-07-23	Login	17:05:12	14	Manage Users
1334	0	2025-07-23	Logout	17:07:35	14	Manage Users
1335	0	2025-07-23	Login	17:07:40	14	Manage Users
1336	0	2025-07-26	Login	10:09:23	14	Manage Users
1337	0	2025-07-28	Login	10:27:58	14	Manage Users
1338	0	2025-07-28	ID: 2071=> Add new failure mode 	10:30:28	14	Failure Mode Identification
1339	0	2025-07-28	ID: 2071=> Delete failure mode 	10:30:56	14	Failure Mode Identification
1340	0	2025-07-28	ID: 28765=> mode_id_id: None to , service_delay: 20 to 10, 	13:57:00	14	Failure Data Collection
1341	0	2025-07-28	ID: 28766=> mode_id_id: None to , service_delay: 20 to 10, 	13:58:07	14	Failure Data Collection
1342	0	2025-07-28	ID: 28767=> mode_id_id: None to , service_delay: 20 to 10, 	13:58:35	14	Failure Data Collection
1343	0	2025-07-28	ID: 28768=> mode_id_id: None to , service_delay: 20 to 10, 	13:59:13	14	Failure Data Collection
1344	0	2025-07-28	ID: 28769=> mode_id_id: None to , service_delay: 20 to 10, 	13:59:26	14	Failure Data Collection
1345	0	2025-07-28	ID: 28770=> mode_id_id: None to , service_delay: 20 to 10, location_id: 1793 to 1797, kilometre_reading: 25000 to 0, 	14:01:28	14	Failure Data Collection
1346	0	2025-07-28	ID: 28771=> mode_id_id: None to , service_delay: 20 to 10, 	14:01:55	14	Failure Data Collection
1347	0	2025-07-28	ID: 28772=> mode_id_id: None to , service_delay: 20 to 10, 	14:02:23	14	Failure Data Collection
1348	0	2025-07-28	ID: 28773=> mode_id_id: None to , service_delay: 20 to 10, 	14:02:50	14	Failure Data Collection
1349	0	2025-07-28	ID: 28774=> mode_id_id: None to , service_delay: 20 to 10, 	14:03:11	14	Failure Data Collection
1350	0	2025-07-28	ID: 28775=> mode_id_id: None to , service_delay: 20 to 10, 	14:03:40	14	Failure Data Collection
1351	0	2025-07-28	ID: 28776=> mode_id_id: None to , service_delay: 20 to 10, 	14:04:17	14	Failure Data Collection
1352	0	2025-07-28	ID: 28777=> mode_id_id: None to , service_delay: 20 to 10, 	14:04:50	14	Failure Data Collection
1353	0	2025-07-28	ID: 28778=> mode_id_id: None to , service_delay: 20 to 10, 	14:05:14	14	Failure Data Collection
1354	0	2025-07-28	ID: 28779=> mode_id_id: None to , service_delay: 20 to 10, 	14:05:44	14	Failure Data Collection
1355	0	2025-07-28	ID: 28780=> mode_id_id: None to , service_delay: 20 to 10, 	14:06:14	14	Failure Data Collection
1356	0	2025-07-28	ID: 28781=> mode_id_id: None to , service_delay: 20 to 10, 	14:06:33	14	Failure Data Collection
1357	0	2025-07-28	ID: 28782=> mode_id_id: None to , service_delay: 20 to 10, 	14:06:58	14	Failure Data Collection
1358	0	2025-07-28	ID: 28783=> mode_id_id: None to , service_delay: 20 to 10, 	14:07:14	14	Failure Data Collection
1359	0	2025-07-28	ID: 28784=> mode_id_id: None to , 	14:07:52	14	Failure Data Collection
1360	0	2025-07-28	ID: 28785=> mode_id_id: None to , service_delay: 20 to 30, 	14:08:21	14	Failure Data Collection
1361	0	2025-07-28	ID: 28786=> mode_id_id: None to , service_delay: 20 to 30, 	14:08:40	14	Failure Data Collection
1362	0	2025-07-28	ID: 28787=> mode_id_id: None to , service_delay: 20 to 30, 	14:09:00	14	Failure Data Collection
1363	0	2025-07-28	ID: 28788=> mode_id_id: None to , service_delay: 20 to 25, 	14:09:25	14	Failure Data Collection
1364	0	2025-07-28	ID: 28789=> mode_id_id: None to , 	14:09:47	14	Failure Data Collection
1365	0	2025-07-28	ID: 28790=> mode_id_id: None to , service_delay: 20 to 30, 	14:10:24	14	Failure Data Collection
1366	0	2025-07-28	ID: 28791=> mode_id_id: None to , service_delay: 20 to 30, 	14:11:01	14	Failure Data Collection
1367	0	2025-07-28	ID: 28792=> mode_id_id: None to , service_delay: 20 to 15, 	14:11:31	14	Failure Data Collection
1368	0	2025-07-28	ID: 28793=> mode_id_id: None to , service_delay: 20 to 15, 	14:12:01	14	Failure Data Collection
1369	0	2025-07-28	ID: 28794=> mode_id_id: None to , service_delay: 20 to 15, 	14:12:30	14	Failure Data Collection
1370	0	2025-07-28	ID: 28795=> mode_id_id: None to , service_delay: 20 to 15, 	14:13:11	14	Failure Data Collection
1371	0	2025-07-28	ID: 28796=> mode_id_id: None to , service_delay: 20 to 30, 	14:13:33	14	Failure Data Collection
1372	0	2025-07-28	ID: 28797=> mode_id_id: None to , service_delay: 20 to 30, 	14:13:58	14	Failure Data Collection
1373	0	2025-07-28	ID: 28798=> mode_id_id: None to , service_delay: 20 to 30, 	14:14:20	14	Failure Data Collection
1374	0	2025-07-28	ID: 28799=> mode_id_id: None to , service_delay: 20 to 30, 	14:14:35	14	Failure Data Collection
1375	0	2025-07-28	ID: 28804=> mode_id_id: None to , service_delay: 20 to 15, 	14:15:16	14	Failure Data Collection
1376	0	2025-07-29	Logout	14:07:35	14	Manage Users
1377	10	2025-07-29	Login	14:35:03	25	Manage Users
1378	10	2025-07-29	ID: 28805=> Add new failure data 	14:41:18	25	Failure Data Collection
1379	10	2025-07-29	ID: 28805=> mode_id_id: None to , 	14:45:13	25	Failure Data Collection
1380	10	2025-07-29	Logout	14:51:12	25	Manage Users
1381	10	2025-07-29	Login	14:51:35	26	Manage Users
1382	10	2025-07-29	Logout	15:02:17	26	Manage Users
1383	10	2025-07-29	Login	15:02:31	25	Manage Users
1384	10	2025-07-29	Logout	15:08:58	25	Manage Users
1385	10	2025-07-29	Login	15:09:10	26	Manage Users
1386	10	2025-07-29	DEFECT ID: 191=> Add new defect 	15:11:44	26	FRACAS Defect Identification
1387	10	2025-07-29	DEFECT ID: 191=> defect_description:  to HVAC not working, investigation:  to Motor found faulty, defect_status_remarks:  to open , defect_status:  to Open, oem_target_date: None to 2025-07-30, defect_open_date: None to 2024-09-30, defect_closed_date: None to None, 	15:13:35	26	FRACAS Defect Identification
1388	10	2025-07-29	ID: 88=> Add new rootcause 	15:17:17	26	Root Cause Analysis
1389	10	2025-07-29	Logout	15:29:21	26	Manage Users
1390	10	2025-07-29	Login	15:30:07	25	Manage Users
1391	10	2025-07-29	Logout	15:33:01	25	Manage Users
1392	10	2025-07-29	Login	15:33:52	27	Manage Users
1393	10	2025-07-29	Logout	16:26:23	27	Manage Users
1394	0	2025-07-29	Login	16:26:35	14	Manage Users
1395	0	2025-07-31	Logout	10:22:00	14	Manage Users
1396	10	2025-07-31	Login	10:22:17	25	Manage Users
1397	10	2025-07-31	Logout	10:57:49	25	Manage Users
1398	0	2025-07-31	Login	10:57:58	14	Manage Users
1399	0	2025-07-31	Logout	15:30:19	14	Manage Users
1400	10	2025-07-31	Login	15:30:27	25	Manage Users
1401	10	2025-07-31	ID: 28765=> mode_id_id: None to , kilometre_reading: 25000 to 160000, 	15:37:29	25	Failure Data Collection
1402	0	2025-07-31	Login	15:47:17	14	Manage Users
1403	10	2025-07-31	ID: 28806=> Add new failure data 	15:49:34	25	Failure Data Collection
1404	10	2025-07-31	Logout	15:54:45	25	Manage Users
1405	10	2025-07-31	Login	15:54:59	26	Manage Users
1406	10	2025-07-31	Logout	16:04:27	26	Manage Users
1407	10	2025-07-31	Login	16:04:33	25	Manage Users
1408	10	2025-07-31	Logout	16:15:59	25	Manage Users
1409	10	2025-07-31	Login	16:16:05	26	Manage Users
1410	10	2025-07-31	DEFECT ID: 192=> Add new defect 	16:16:58	26	FRACAS Defect Identification
1411	10	2025-07-31	DEFECT ID: 192=> defect_description:  to filter grill is defected, investigation:  to inspection, defect_status_remarks:  to open , defect_status:  to Open, oem_target_date: None to 2025-08-05, defect_open_date: None to 2025-07-31, defect_closed_date: None to None, 	16:19:56	26	FRACAS Defect Identification
1412	10	2025-07-31	ID: 89=> Add new rootcause 	16:25:20	26	Root Cause Analysis
1413	10	2025-07-31	DEFECT ID: 193=> Add new defect 	17:08:44	26	FRACAS Defect Identification
1414	10	2025-07-31	DEFECT ID: 193=> defect_description:  to *Defect description:, investigation:  to \n*Defect description:\n*Investigation:, defect_status_remarks:  to Defect status remarks, defect_status:  to Open, oem_target_date: None to 2025-12-18, defect_open_date: None to 2025-07-25, defect_closed_date: None to None, 	17:09:28	26	FRACAS Defect Identification
1415	10	2025-07-31	ID: 90=> Add new rootcause 	17:11:00	26	Root Cause Analysis
1416	10	2025-07-31	Logout	17:13:59	26	Manage Users
1417	0	2025-07-31	Login	17:14:05	14	Manage Users
1418	0	2025-07-31	Logout	17:14:37	14	Manage Users
1419	10	2025-07-31	Login	17:14:43	26	Manage Users
1420	10	2025-07-31	Logout	18:18:45	26	Manage Users
1421	10	2025-07-31	Login	18:18:51	25	Manage Users
1422	10	2025-07-31	Logout	18:27:27	25	Manage Users
1423	10	2025-07-31	Login	18:27:36	25	Manage Users
1424	10	2025-07-31	Logout	18:29:13	25	Manage Users
1425	0	2025-08-01	Login	09:47:49	14	Manage Users
1426	0	2025-08-01	Login	09:53:07	14	Manage Users
1427	0	2025-08-01	USERNAME: rajkumaranumula@titagarh.in=> Add new user 	14:08:36	14	Manage Users
1428	0	2025-08-01	Logout	14:08:55	14	Manage Users
1429	10	2025-08-01	Login	14:09:13	30	Manage Users
1430	10	2025-08-01	Logout	14:09:22	30	Manage Users
1431	0	2025-08-01	Login	14:10:34	14	Manage Users
1432	0	2025-08-01	USERNAME: mahendra.jadaun@titagarh.in=> Add new user 	14:13:51	14	Manage Users
1433	0	2025-08-01	Logout	14:13:54	14	Manage Users
1434	10	2025-08-01	Login	14:14:08	31	Manage Users
1435	10	2025-08-01	Logout	14:14:24	31	Manage Users
1436	0	2025-08-01	Login	14:14:36	14	Manage Users
1437	0	2025-08-01	USERNAME: sandeep.jadhav@titagarh.in=> Add new user 	14:16:34	14	Manage Users
1438	0	2025-08-01	Logout	14:16:37	14	Manage Users
1439	10	2025-08-01	Login	14:16:55	32	Manage Users
1440	10	2025-08-01	Logout	14:17:07	32	Manage Users
1441	0	2025-08-01	Login	14:17:13	14	Manage Users
1442	0	2025-08-01	USERNAME: narayan.verma@titagarh.in=> Add new user 	14:18:24	14	Manage Users
1443	0	2025-08-01	Logout	14:18:28	14	Manage Users
1444	10	2025-08-01	Login	14:18:42	33	Manage Users
1445	10	2025-08-01	Logout	14:18:46	33	Manage Users
1446	0	2025-08-01	Login	14:19:05	14	Manage Users
1447	0	2025-08-01	USERNAME: abhishek.verma@titagarh.in=> Add new user 	14:20:10	14	Manage Users
1448	0	2025-08-01	Logout	14:20:36	14	Manage Users
1449	10	2025-08-01	Login	14:20:49	34	Manage Users
1450	10	2025-08-01	Logout	14:20:58	34	Manage Users
1451	0	2025-08-01	Login	14:21:04	14	Manage Users
1452	0	2025-08-01	USERNAME: ramesh.bhukya@titagarh.in=> Add new user 	14:22:28	14	Manage Users
1453	0	2025-08-01	Logout	14:22:36	14	Manage Users
1454	10	2025-08-01	Login	14:22:49	35	Manage Users
1455	0	2025-08-01	Login	14:35:26	14	Manage Users
1456	10	2025-08-01	Logout	15:02:23	35	Manage Users
1457	0	2025-08-01	Login	15:02:29	14	Manage Users
1458	0	2025-08-01	Logout	15:06:30	14	Manage Users
1459	10	2025-08-01	Login	15:06:34	25	Manage Users
1460	10	2025-08-01	Logout	15:08:59	25	Manage Users
1461	0	2025-08-01	Login	15:09:15	14	Manage Users
1462	0	2025-08-01	Logout	16:53:53	14	Manage Users
1463	0	2025-08-01	Login	18:23:26	14	Manage Users
1464	0	2025-08-02	Logout	10:04:54	14	Manage Users
1465	0	2025-08-02	ID: 2072=> Add new failure mode 	10:18:00	14	Failure Mode Identification
1466	0	2025-08-02	Login	10:36:16	14	Manage Users
1467	0	2025-08-02	Logout	13:36:29	14	Manage Users
1468	0	2025-08-02	Login	13:36:37	14	Manage Users
1469	0	2025-08-02	USERNAME: mahtab.alam@titagarh.in=> Add new user 	13:44:44	14	Manage Users
1470	0	2025-08-02	Logout	13:44:48	14	Manage Users
1471	10	2025-08-02	Login	13:45:09	36	Manage Users
1472	10	2025-08-02	Logout	13:46:36	36	Manage Users
1473	10	2025-08-02	Login	13:46:58	36	Manage Users
1474	10	2025-08-02	Logout	13:47:02	36	Manage Users
1475	0	2025-08-02	Login	13:47:07	14	Manage Users
1476	0	2025-08-02	Logout	13:47:26	14	Manage Users
1477	10	2025-08-02	Login	13:47:43	36	Manage Users
1478	10	2025-08-02	Logout	13:53:12	36	Manage Users
1479	0	2025-08-02	Login	13:53:17	14	Manage Users
1480	0	2025-08-02	Logout	13:57:02	14	Manage Users
1481	10	2025-08-02	Login	13:57:19	35	Manage Users
1482	10	2025-08-02	Logout	13:57:44	35	Manage Users
1483	10	2025-08-02	Login	13:58:25	30	Manage Users
1484	10	2025-08-02	Logout	13:59:39	30	Manage Users
1485	0	2025-08-02	Login	13:59:47	14	Manage Users
1486	0	2025-08-02	Logout	14:02:40	14	Manage Users
1487	10	2025-08-02	Login	14:02:53	36	Manage Users
1488	0	2025-08-02	Logout	14:04:27	14	Manage Users
1489	10	2025-08-02	Login	14:04:48	35	Manage Users
1490	10	2025-08-02	Logout	14:05:40	36	Manage Users
1491	0	2025-08-02	Login	14:05:51	14	Manage Users
1492	0	2025-08-02	Logout	14:06:16	14	Manage Users
1493	10	2025-08-02	Login	14:06:40	31	Manage Users
1494	10	2025-08-02	Logout	14:11:12	31	Manage Users
1495	10	2025-08-02	Logout	14:21:15	35	Manage Users
1496	0	2025-08-02	Login	16:00:37	14	Manage Users
1497	0	2025-08-02	Logout	16:08:19	14	Manage Users
1498	10	2025-08-02	Login	16:46:34	26	Manage Users
1499	10	2025-08-02	Logout	16:48:44	26	Manage Users
1500	0	2025-08-02	Login	16:48:54	14	Manage Users
1501	0	2025-08-02	Logout	17:02:59	14	Manage Users
1502	0	2025-08-02	Login	18:17:20	14	Manage Users
1503	0	2025-08-02	DEFECT ID: 194=> Add new defect 	18:19:29	14	FRACAS Defect Identification
1504	0	2025-08-02	DEFECT ID: 194=> defect_description:  to sgshsh, investigation:  to snananb, defect_status_remarks:  to open, defect_status:  to Open, oem_target_date: None to 2025-08-31, defect_open_date: None to 2025-07-10, defect_closed_date: None to None, 	18:21:53	14	FRACAS Defect Identification
1505	0	2025-08-03	Logout	15:14:49	14	Manage Users
1506	10	2025-08-03	Login	15:15:11	35	Manage Users
1507	0	2025-08-04	Login	10:08:26	14	Manage Users
1508	10	2025-08-04	Logout	10:19:53	35	Manage Users
1509	0	2025-08-04	Login	10:20:00	14	Manage Users
1510	0	2025-08-04	Logout	11:48:40	14	Manage Users
1511	0	2025-08-04	Login	13:45:11	14	Manage Users
1512	0	2025-08-04	Logout	13:49:05	14	Manage Users
1513	0	2025-08-04	Login	13:55:15	14	Manage Users
1514	0	2025-08-04	Logout	13:55:22	14	Manage Users
1515	0	2025-08-04	Login	13:55:44	14	Manage Users
1516	0	2025-08-04	Logout	13:55:47	14	Manage Users
1517	0	2025-08-04	Login	13:58:19	14	Manage Users
1518	0	2025-08-04	Logout	13:58:24	14	Manage Users
1519	0	2025-08-04	Login	13:59:12	14	Manage Users
1520	0	2025-08-04	Logout	14:02:39	14	Manage Users
1521	0	2025-08-04	Logout	14:05:04	14	Manage Users
1522	0	2025-08-04	Login	14:06:30	14	Manage Users
1523	0	2025-08-04	Login	14:18:57	14	Manage Users
1524	0	2025-08-04	Logout	14:24:52	14	Manage Users
1525	0	2025-08-04	Login	14:25:11	14	Manage Users
1526	0	2025-08-04	Logout	14:26:10	14	Manage Users
1527	0	2025-08-04	Logout	14:27:48	14	Manage Users
1528	0	2025-08-04	Login	14:28:09	14	Manage Users
1529	0	2025-08-04	Logout	14:36:02	14	Manage Users
1530	0	2025-08-04	Login	16:03:16	14	Manage Users
1531	0	2025-08-04	Logout	16:15:46	14	Manage Users
1532	0	2025-08-04	Login	17:00:09	14	Manage Users
1533	0	2025-08-04	ID: 90=> failure_detection:  to TS, 	17:36:47	14	Root Cause Analysis
\.


--
-- Data for Name: fracas_investigationdetails; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_investigationdetails (details_id, non_compliance_details, onvestigation_details, "relevant_ERTS_clause", is_active, eir_dt_id_id) FROM stdin;
1	*Non- compliance details:	*Investigation Details:	*Relevant ERTS clause:	0	1
2	thee	investigation	relevent	0	1
\.


--
-- Data for Name: fracas_jobcard; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_jobcard (job_id, train_set_no, date, "time", department, subsystem, equipment, job_description, nature_of_job, sic_required, assigned_to, last_update, status, job_card_no, run_status, ohe_required, issued_to, completion_time, from_revenue_service, delay_to_service, trip_no, event_date, event_time, sic_no, failure_id_id, issued_by, l1_date, l1_time, signature_img, l2_date, l2_time, received_by, signature_img2, follow_up_details, handed_over, new_supervisor, signature_img3, completion_date, completion_date_time, completion_name, down_time, signature_img4, train_can_be_energized, train_can_be_moved, completion_date2, completion_date_time2, completion_name2, corrective_action, down_time2, sic_has_performed, sic_start_time, signature_img5, train_can_be_energized2, train_can_be_moved2, details_of_the_activitues, close_date, close_name, close_time, signature_img6) FROM stdin;
21	1785	2024-08-15	22:30:00	Maintainer		CI-2	\N	\N	\N	\N	2025-07-08	0	RST/07-2025/0017	0		\N					\N	\N		28765		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
22	1786	2024-08-15	22:30:00	Maintainer		CI-2	\N	\N	\N	\N	2025-07-08	0	RST/07-2025/0018	0		\N					\N	\N		28766		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
8	1774	2024-08-19	16:28:00	Operator		HVAC	\N		Yes	None	2025-07-02	1	RST/07-2025/0004	8	No	Amir	3	No			2024-08-19	16:28:00		28752	Vinod Yadav	2024-08-19	16:28:00	/home/assetoptima/pune_metro_jobcard/static/uploads/039.png	2024-08-19	16:30:00	Anas Khan	/home/assetoptima/pune_metro_jobcard/static/uploads/040.png	None	No	Gautam	/home/assetoptima/pune_metro_jobcard/static/uploads/038.png	2024-08-19	18:30:00	Anas Khan	0	/home/assetoptima/pune_metro_jobcard/static/uploads/040.png	Yes	Yes	2024-08-19	18:25:00	Hari	SIC has been done	20	1	18:05	/home/assetoptima/pune_metro_jobcard/static/uploads/031.png	Yes	Yes	HVAC Drain extension hose pipe has been installed	2024-08-19	Vinod Yadav	18:35:00	/home/assetoptima/pune_metro_jobcard/static/uploads/038.png
18	1775	2024-08-19	09:46:00	Operator		DCU	\N	\N	\N	\N	2025-07-04	0	RST/07-2025/0014	0		\N					\N	\N		28762		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
4	1771	2025-06-27	12:30:00	Operator		Lense	\N	Schedule Preventive Maintenance	Yes	None	2025-06-27	0	RST/06-2025/0004	7	No	xyz	3	Yes	30		2025-06-27	12:37:00		28748	None	2025-07-01	10:38:00	/home/assetoptima/pune_metro_jobcard/static/uploads/30.png	2025-07-01	10:40:00	none	/home/assetoptima/pune_metro_jobcard/static/uploads/JC-2.png	None	No			2025-07-01	10:55:00	none		/home/assetoptima/pune_metro_jobcard/static/uploads/JC-1.png	Yes	Yes	2025-07-01	10:56:00	none	None		1		/home/assetoptima/pune_metro_jobcard/static/uploads/JC-1.png	Yes	Yes	None	2025-07-01	none	10:57:00	/home/assetoptima/pune_metro_jobcard/static/uploads/JC-1.png
1	1771	2025-06-23	15:03:00	Operator		camera	\N	Schedule Preventive Maintenance	Yes	None	2025-06-23	1	RST/06-2025/0001	8	Yes	ram	3	No			2025-06-12	16:13:00		28745	amir	2025-06-23	15:48:00	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	2025-06-24	16:50:00	amir	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	None	Yes			2025-06-23	16:56:00	amir	00:30	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	Yes	Yes	2025-06-23	15:57:00	amir	SIC has been done	00:30	1	17:58	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	Yes	Yes	camera has been changed 	2025-06-24	amir 	16:59:00	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg
5	1784	2024-08-28	09:30:00	Operator		TCMS	\N	\N	\N	\N	2025-07-02	0	RST/07-2025/0001	0		\N					\N	\N		28749		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
2	1772	2025-06-23	16:07:00	Operator		Hinge 	\N	Overhaul	Yes	None	2025-06-23	0	RST/06-2025/0002	2	Yes	None	3	Yes			2025-06-12	17:14:00		28746		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
3	1771	2025-06-25	15:23:00	Operator		camera	\N	\N	\N	\N	2025-06-25	0	RST/06-2025/0003	0		\N					\N	\N		28747		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
9	1775	2024-08-15	00:30:00	Operator		DCU	\N	\N	\N	\N	2025-07-02	0	RST/07-2025/0005	0		\N					\N	\N		28753		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
10	1776	2024-08-15	00:30:00	Operator		SCU	\N	\N	\N	\N	2025-07-02	0	RST/07-2025/0006	0		\N					\N	\N		28754		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
11	1777	2024-08-15	00:30:00	Operator		MDS	\N	\N	\N	\N	2025-07-02	0	RST/07-2025/0007	0		\N					\N	\N		28755		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
12	1778	2024-08-15	00:30:00	Operator		DRM	\N	\N	\N	\N	2025-07-02	0	RST/07-2025/0008	0		\N					\N	\N		28756		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
13	1779	2024-08-15	00:30:00	Operator		DCU	\N	\N	\N	\N	2025-07-02	0	RST/07-2025/0009	0		\N					\N	\N		28757		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
14	1780	2024-08-15	00:30:00	Operator		DCU	\N	\N	\N	\N	2025-07-02	0	RST/07-2025/0010	0		\N					\N	\N		28758		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
15	1781	2024-08-15	00:30:00	Operator		DCU	\N	\N	\N	\N	2025-07-02	0	RST/07-2025/0011	0		\N					\N	\N		28759		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
16	1782	2024-08-15	00:30:00	Operator		DRM	\N	\N	\N	\N	2025-07-02	0	RST/07-2025/0012	0		\N					\N	\N		28760		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
17	1783	2024-08-23	05:00:00	Operator		Camera	\N	\N	\N	\N	2025-07-02	0	RST/07-2025/0013	0		\N					\N	\N		28761		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
20	1783	2025-07-03	11:31:00	Operator		camera	\N		Yes	None	2025-07-04	1	RST/07-2025/0016	8	Yes	None	1	Yes			2025-07-04	11:35:00		28764	mihir	2025-07-04	11:37:00	/home/assetoptima/pune_metro_jobcard/static/uploads/IMG_9573.JPG	2025-07-04	11:39:00	mihir	/home/assetoptima/pune_metro_jobcard/static/uploads/IMG_9573.JPG	None	No			2025-07-04	11:41:00	mihir		/home/assetoptima/pune_metro_jobcard/static/uploads/IMG_9573.JPG	Yes	Yes	2025-07-04	11:41:00	mihir	None		1		/home/assetoptima/pune_metro_jobcard/static/uploads/IMG_9573.JPG	Yes	Yes	None	2025-07-04	mihir	11:42:00	/home/assetoptima/pune_metro_jobcard/static/uploads/IMG_9573.JPG
23	1787	2024-08-15	22:30:00	Operator		CI-2	\N	\N	\N	\N	2025-07-08	0	RST/07-2025/0019	0		\N					\N	\N		28767		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
24	1788	2024-08-15	22:30:00	Operator		CI-2	\N	\N	\N	\N	2025-07-08	0	RST/07-2025/0020	0		\N					\N	\N		28768		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
19	1775	2025-07-03	11:06:00	Operator		camera	\N		Yes	None	2025-07-04	1	RST/07-2025/0015	8	Yes	None	5	Yes			2025-07-04	11:12:00		28763	mihir	2025-07-04	11:14:00	/home/assetoptima/pune_metro_jobcard/static/uploads/IMG_9573.JPG	2025-07-04	11:16:00	mihir	/home/assetoptima/pune_metro_jobcard/static/uploads/IMG_9573.JPG	None	No			2025-07-04	11:19:00	mihir		/home/assetoptima/pune_metro_jobcard/static/uploads/IMG_9573.JPG	Yes	Yes	2025-07-04	11:19:00	mihir	None		1		/home/assetoptima/pune_metro_jobcard/static/uploads/IMG_9573.JPG	Yes	Yes	None	2025-07-04	mihir	11:21:00	/home/assetoptima/pune_metro_jobcard/static/uploads/IMG_9573.JPG
25	1789	2024-08-15	22:30:00	Operator		CI-2	\N	\N	\N	\N	2025-07-08	0	RST/07-2025/0021	0		\N					\N	\N		28769		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
26	1793	2024-08-28	22:20:00	Maintainer		Partition Door 	\N	\N	\N	\N	2025-07-08	0	RST/07-2025/0022	0		\N					\N	\N		28770		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
27	1800	2024-09-08	10:10:00	Operator		Compressor 	\N	\N	\N	\N	2025-07-08	0	RST/07-2025/0023	0		\N					\N	\N		28771		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
28	1801	2024-08-29	11:30:00	Operator		HVAC-01	\N	\N	\N	\N	2025-07-08	0	RST/07-2025/0024	0		\N					\N	\N		28772		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
29	1802	2024-08-29	11:30:00	Operator		HVAC-02	\N	\N	\N	\N	2025-07-08	0	RST/07-2025/0025	0		\N					\N	\N		28773		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
30	1790	2024-08-30	22:10:00	Maintainer		Announcements	\N	\N	\N	\N	2025-07-08	0	RST/07-2025/0026	0		\N					\N	\N		28774		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
31	1799	2024-08-30	22:10:00	Maintainer		PA/PIS	\N	\N	\N	\N	2025-07-08	0	RST/07-2025/0027	0		\N					\N	\N		28775		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
32	1803	2024-08-30	22:10:00	Maintainer		PA/PIS	\N	\N	\N	\N	2025-07-08	0	RST/07-2025/0028	0		\N					\N	\N		28776		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
33	1804	2024-08-13	22:30:00	Maintainer		MDS/CCTV	\N	\N	\N	\N	2025-07-08	0	RST/07-2025/0029	0		\N					\N	\N		28777		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
34	1805	2024-08-13	22:30:00	Maintainer		CI-2	\N	\N	\N	\N	2025-07-08	0	RST/07-2025/0030	0		\N					\N	\N		28778		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
35	1806	2024-08-13	22:30:00	Operator		HVAC Unit -1	\N	\N	\N	\N	2025-07-08	0	RST/07-2025/0031	0		\N					\N	\N		28779		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
36	1807	2024-08-13	22:30:00	Maintainer		TCMS	\N	\N	\N	\N	2025-07-08	0	RST/07-2025/0032	0		\N					\N	\N		28780		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
37	1809	2024-08-13	22:30:00	Operator		TCMS	\N	\N	\N	\N	2025-07-08	0	RST/07-2025/0033	0		\N					\N	\N		28781		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
38	1810	2024-08-13	22:30:00	Maintainer		Saloon Door 	\N	\N	\N	\N	2025-07-08	0	RST/07-2025/0034	0		\N					\N	\N		28782		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
39	1792	2024-08-12	22:10:00	Maintainer		Saloon Door 	\N	\N	\N	\N	2025-07-08	0	RST/07-2025/0035	0		\N					\N	\N		28783		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
40	1808	2024-08-21	23:50:00	Operator		HVAC	\N	\N	\N	\N	2025-07-09	0	RST/07-2025/0036	0		\N					\N	\N		28784		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
41	1812	2024-08-25	14:00:00	Operator		HVAC	\N	\N	\N	\N	2025-07-09	0	RST/07-2025/0037	0		\N					\N	\N		28785		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
42	1813	2024-08-25	14:00:00	Operator		HVAC	\N	\N	\N	\N	2025-07-09	0	RST/07-2025/0038	0		\N					\N	\N		28786		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
43	1815	2024-08-25	14:00:00	Operator		HVAC	\N	\N	\N	\N	2025-07-09	0	RST/07-2025/0039	0		\N					\N	\N		28787		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
45	1962	2024-08-25	15:00:00	Operator		MDS	\N	\N	\N	\N	2025-07-09	0	RST/07-2025/0041	0		\N					\N	\N		28789		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
46	1963	2024-08-25	15:25:00	Operator		HVAC	\N	\N	\N	\N	2025-07-09	0	RST/07-2025/0042	0		\N					\N	\N		28790		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
47	1964	2024-08-25	15:25:00	Operator		Wiper	\N	\N	\N	\N	2025-07-09	0	RST/07-2025/0043	0		\N					\N	\N		28791		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
48	1965	2024-08-25	07:11:00	Operator		BECU	\N	\N	\N	\N	2025-07-09	0	RST/07-2025/0044	0		\N					\N	\N		28792		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
49	1966	2024-08-25	07:11:00	Operator		FDU	\N	\N	\N	\N	2025-07-09	0	RST/07-2025/0045	0		\N					\N	\N		28793		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
50	1967	2024-08-25	12:16:00	Operator		Cab Door	\N	\N	\N	\N	2025-07-09	0	RST/07-2025/0046	0		\N					\N	\N		28794		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
51	1968	2024-08-25	08:10:00	Operator		CCTV	\N	\N	\N	\N	2025-07-09	0	RST/07-2025/0047	0		\N					\N	\N		28795		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
52	1973	2024-08-05	10:40:00	Operator		Car Door	\N	\N	\N	\N	2025-07-09	0	RST/07-2025/0048	0		\N					\N	\N		28796		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
53	1977	2024-09-06	10:00:00	Operator		Car Door	\N	\N	\N	\N	2025-07-09	0	RST/07-2025/0049	0		\N					\N	\N		28797		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
54	1978	2024-09-06	10:00:00	Operator		HVAC	\N	\N	\N	\N	2025-07-09	0	RST/07-2025/0050	0		\N					\N	\N		28798		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
55	1985	2024-09-06	10:00:00	Operator		HVAC	\N	\N	\N	\N	2025-07-09	0	RST/07-2025/0051	0		\N					\N	\N		28799		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
56	1986	2024-09-07	22:00:00	Operator		HVAC	\N	\N	\N	\N	2025-07-09	0	RST/07-2025/0052	0		\N					\N	\N		28800		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
57	1987	2024-09-07	22:00:00	Operator		Pantograph	\N	\N	\N	\N	2025-07-09	0	RST/07-2025/0053	0		\N					\N	\N		28801		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
58	1988	2024-09-08	22:00:00	Operator		Emergency Door	\N	\N	\N	\N	2025-07-09	0	RST/07-2025/0054	0		\N					\N	\N		28802		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
59	1989	2024-09-08	22:00:00	Operator		VCC	\N	\N	\N	\N	2025-07-09	0	RST/07-2025/0055	0		\N					\N	\N		28803		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
60	1990	2024-09-10	09:13:00	Operator		PA/PIS	\N	\N	\N	\N	2025-07-09	0	RST/07-2025/0056	0		\N					\N	\N		28804		\N	\N	\N	\N	\N		\N	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
7	1773	2024-08-19	16:28:00	Operator		BECU	\N		Yes	None	2025-07-02	1	RST/07-2025/0003	8	No	None	3	No			2024-08-19	16:28:00		28751	Vinod Yadav	2024-08-19	16:30:00	/home/assetoptima/pune_metro_jobcard/static/uploads/JC 3.png	2024-08-19	16:30:00	Anas Khan	/home/assetoptima/pune_metro_jobcard/static/uploads/4.png	None	No	Gautam	/home/assetoptima/pune_metro_jobcard/static/uploads/4.png	2024-08-19	18:30:00	Anas Khan	0	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	Yes	Yes	2024-08-19	18:25:00	Hari	None	20	1	18:05	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	Yes	Yes	None	2024-08-19	Vinod Yadav	18:35:00	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg
6	1773	2024-08-19	16:28:00	Operator		BECU	\N		Yes	None	2025-07-02	1	RST/07-2025/0002	8	Yes	None	3	Yes			2025-07-15	18:49:00		28750	amir	2025-07-15	13:59:00	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	2025-07-19	17:13:00	amir	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	None	No	amir	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	2025-07-19	17:15:00	amir	30	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	Yes	Yes	2025-07-19	17:14:00	amir	None	30	1		/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	Yes	Yes	None	2025-07-19	amir 	17:14:00	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg
44	1959	2024-08-25	14:50:00	Operator		HVAC	\N	Schedule Preventive Maintenance	Yes	None	2025-07-09	0	RST/07-2025/0040	4	Yes	Maintainer	3	Yes	30		2025-07-15	18:06:00		28788	amir	2025-08-03	15:11:00	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	2025-08-04	18:33:00	amir	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	\N			\N	\N	\N			\N			\N	\N		\N				\N			\N	\N		\N	\N
61	1986	2025-07-29	14:36:00	Operator		HVAC	\N	Schedule Preventive Maintenance	Yes	None	2025-07-29	1	RST/07-2025/0057	8	Yes	Maintainer	2	Yes	10		2025-07-22	12:45:00		28805	amir	2025-07-30	15:52:00	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	2025-07-31	10:30:00	ashik	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	None	No	Ashik	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	2025-07-31	12:54:00	Amir	10	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	Yes	Yes	2025-07-29	16:01:00	ashik	None	10	1		/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	Yes	Yes	Successfully Changed the HVAC system.	2025-07-29	amir	17:04:00	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg
62	1808	2025-07-31	15:31:00	Operator		HVAC	\N	Schedule Preventive Maintenance	Yes	None	2025-07-31	1	RST/07-2025/0058	8	Yes	Maintainer	1	No			2025-07-31	15:45:00		28806	matab	2025-07-31	15:54:00	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	2025-07-31	16:22:00	ashik	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	None	No			2025-07-31	16:05:00	Amir	20	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	Yes	Yes	2025-07-31	16:10:00	ashik	None	20	1	16:05	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	Yes	Yes	None	2025-07-31	amir	17:00:00	/home/assetoptima/pune_metro_jobcard/static/uploads/WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg
\.


--
-- Data for Name: fracas_jobcardids; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_jobcardids (uid_id, year, month, last_id) FROM stdin;
1	2025	6	4
2	2025	7	58
\.


--
-- Data for Name: fracas_jobdetails; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_jobdetails (job_details_id, s_no, job_description, is_active, job_card_id_id) FROM stdin;
1		Change the camera and do the need full Maintenace 	0	1
2		change the hinges	0	2
3		yeh	0	4
4		HVAC drainage pipe extension hose pipe rust	0	8
5		Pressure Governer cover to be installed	0	7
6		none	0	19
7		none	0	20
8		none	0	20
9		brake pads has been replaced	0	6
10		Schedule a preventive maintenance of HVAC system	0	61
11		Need to change the air filter	0	62
12		job 	0	44
\.


--
-- Data for Name: fracas_jobreplacedequipment; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_jobreplacedequipment (job_equipment_id, jobequipment_name, jobequipment_new_no, jobequipment_old_no, is_active, job_card_id_id) FROM stdin;
1	Nil	Nil	Nil	0	7
\.


--
-- Data for Name: fracas_jobworktomaintainers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_jobworktomaintainers (job_work_id, jobwork_name, jobwork_work, jobwork_signature, is_active, job_card_id_id) FROM stdin;
1	rakesh	inspection 	amir	0	1
2	rohan	equipment changing	amir	0	1
3	Gowri	Nil	Nil	0	7
4	mihir	none	mihir	0	19
5	none	none	none	1	20
6	mihir	none	mihir	0	20
7	rakesh	regular Maintenace	WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	0	6
8	amir	Change the HVAC system 	WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	0	61
9	amir	clean filter	WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	0	62
\.


--
-- Data for Name: fracas_kilometrereading; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_kilometrereading (km_id, date, ts01_tkm, ts02_tkm, ts03_tkm, ts04_tkm, ts05_tkm, ts06_tkm, ts07_tkm, ts08_tkm, ts09_tkm, ts10_tkm, ts11_tkm, ts12_tkm, ts13_tkm, ts14_tkm, ts15_tkm, ts16_tkm, ts17_tkm, ts18_tkm, ts19_tkm, ts20_tkm, ts21_tkm, ts22_tkm, ts23_tkm, ts24_tkm, ts25_tkm, ts26_tkm, ts27_tkm, ts28_tkm, ts29_tkm, ts30_tkm, ts31_tkm, ts32_tkm, ts33_tkm, ts34_tkm) FROM stdin;
1	2024-08-01	119611	120847	119231	0	138895	104578	0	0	0	0	100438	77001	73275	91338	0	0	54858	0	47194	54229	0	0	0	0	0	0	0	0	0	0	0	0	0	0
2	2024-08-02	119870	121165	119611	0	139258	104578	0	0	0	0	100826	77375	73458	91759	0	0	55220	0	47524	54321	0	0	0	0	0	0	0	0	0	0	0	0	0	0
3	2024-08-06	120987	122120	120977	0	140368	105817	0	0	0	0	101885	78631	74955	92936	0	0	56211	0	48191	54431	0	0	0	0	0	0	3215	3308	2197	2252	777	0	0	0
4	2024-08-07	121361	122512	121343	0	140368	106148	0	0	0	0	102155	78762	75229	93087	0	0	56600	0	48407	54469	0	0	0	0	0	0	3575	3637	2230	2252	777	0	0	0
5	2024-08-09	122008	123228	121343	0	140368	106838	0	0	0	0	102394	19049	75875	93621	0	0	57115	0	49155	54889	0	0	0	0	0	0	4160	4151	2230	2522	777	0	0	0
6	2024-08-10	122397	123228	121343	0	140368	107169	0	0	0	0	102784	79439	75875	93995	0	0	57360	0	49442	55135	0	0	0	0	0	0	4518	4482	2230	2793	777	0	0	0
7	2024-08-11	122520	123775	121649	0	141031	107834	0	0	0	0	103564	79439	76266	94729	0	0	58092	0	50161	55619	0	0	0	0	0	0	4900	4814	2230	3276	777	0	0	0
8	2024-08-12	122520	123775	122003	0	141031	108104	0	0	0	0	103778	79439	76750	95118	0	0	58350	0	50534	55980	0	0	0	0	0	0	4900	5146	2271	3276	777	0	0	0
9	2024-08-13	122520	123775	122384	0	141278	108332	0	0	0	0	103778	79825	76570	95450	0	0	58737	0	50908	56223	0	0	0	0	0	0	5623	5595	2271	3966	777	0	0	0
10	2024-08-14	122882	123775	122624	0	141278	108591	0	0	0	0	103778	79825	76845	95823	0	0	59099	0	51268	56613	0	0	0	0	0	0	5893	5925	2271	4295	777	0	0	0
11	2024-08-15	123272	123775	122716	0	141278	108923	0	0	0	0	103778	80276	76845	96111	0	0	59375	0	51599	56943	0	0	0	0	0	0	6253	6195	2271	4668	777	0	0	0
12	2024-08-19	123994	124526	123484	0	142119	10992	0	0	0	0	104563	81121	76845	96111	0	0	60340	0	52178	57937	0	0	0	0	0	0	7428	7186	2271	5137	777	0	0	0
13	2024-08-20	123994	124918	123809	0	142272	10992	0	0	0	0	104894	81510	77205	96111	0	0	60671	0	52552	58212	0	0	0	0	0	0	7428	7402	2271	5410	777	0	0	0
14	2024-08-22	123994	125581	124313	0	142935	110544	0	0	0	0	105498	81872	77810	96596	0	0	60671	0	54840	58814	0	0	0	0	0	0	8193	7827	2271	6041	777	0	0	0
15	2024-08-25	123994	126730	125552	0	144113	111204	0	0	0	0	105756	83106	79016	97683	0	0	6170	0	54236	59392	0	0	0	0	0	0	9201	9000	2487	7305	777	0	0	0
16	2024-08-26	123994	127002	125818	0	144473	111204	0	0	0	0	105880	83106	79376	97986	0	0	61884	0	54609	59666	0	0	0	0	0	0	9201	9272	2519	7665	777	0	0	0
17	2024-08-27	123994	121216	125818	0	144802	111365	0	0	0	0	106110	83854	79648	98345	0	0	62244	0	54762	59814	0	0	0	0	0	0	9474	9272	2823	8024	777	0	0	0
18	2024-08-28	124018	127518	125999	0	145162	111365	0	0	0	0	106001	84128	79919	98345	0	0	62517	0	55123	60085	0	0	0	0	0	0	9474	10019	3182	8294	819	0	0	0
19	2024-08-29	124018	127792	126209	0	145436	111724	0	0	0	0	106001	84504	80162	98345	0	0	62877	0	55396	60085	0	0	0	0	0	0	10224	10318	3543	8565	819	0	0	0
20	2024-09-01	124018	128486	126774	0	146378	112604	0	0	0	0	106001	85488	81100	98345	0	0	63874	0	56153	60813	0	0	0	0	0	0	11069	11185	4181	9503	819	0	0	0
\.


--
-- Data for Name: fracas_ncrgeneration; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_ncrgeneration (rec_id, ncr_gen_id, date, "time", is_active, rootcause_id_id, action_date, approved_date, corrective_action_date, defect_date, fnl_date, verification_date, defect_time, defect_description, assembly_name, assembly_no, detection_workstation, drawing_no, green_red_channel, inspector_name, location_id, sel_car, serial_no, "chkCritical", "chkMajor", "chkMinor", defect_detected_by, defect_detected_workstation, defect_location, defect_source, no_of_defective_parts, no_of_parts_deloverd, specification, supplier_name, active_deviations, "chk_Internal", "chk_Supplier", "chk_TWL", "chk_Transportation", notok_img, ok_img, signature_img, signature_img2, signature_img3, signature_img4, signature_img5, action_name, approved_by, approved_designation, attachments_files, containment_action, corrective_action_by, corrective_action_designation, detection, effectiveness, initial_analysis, inp_root_cause, invoice_number, non_conforming_part_disposition, occurrence, responsibility, responsible_for_execution, verification_name, cost_1, cost_2, cost_3, cost_4, cost_5, cost_6, total_cost, fnl_designation, fnl_name, no_of_day_open, physical_closure, physical_closure_rca_capa, asset_type, ncr_status, root_cause_analysis, rev_no, rejection_status, remark, accept_status) FROM stdin;
1	TWLPune-RS-ML-NCR-2025/001	2025-07-15	10:51:09	0	87	2025-07-15	2025-07-15	2025-07-15	2024-11-28	2025-07-18	2025-07-15	11:30	Oil Seepage from CRANKSHAFT COUPLING SIDE AREA	CI-2	8.120.2.321.227.9	MainLine	MP1586000MF01	Red	SOURAV JANA 	TS#16	DMB	Cl 2 - 16	0	1	0	Sandeep 		TS#23 DMB	Main Line			Should not be seepage 	KBI		0	0	0	0	\N	\N	WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	amir	Gulam	engineer	Yes	Done	amir	engineer										gulam	0	0	0	0	0	0	0	engineer	AMIR RIZVI	3			CI-2	0	Not necessary	0	1	out of warranty	0
2	TWLPune-RS-ML-NCR-2025/002	2025-07-29	15:17:17	0	88	2025-07-29	2025-07-30	2025-07-29	2024-09-30	2025-12-31	2025-07-30	15:17	HVAC not working	HVAC	12545			Green	amir	TS#03, TS#04, TS#05	DMA, TC	HVAC-03	0	0	1	ashik		location car	Schedule Preventive Maintenance	1		rubber is defective	KSBI		0	1	0	0	\N	\N	WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	amir	amir	lead maintainer	Yes	Done	ashik	lead maintainer		as rubber was changed now motor is working properly in HVAC 	1mm damage can be seen on the rubber presented in motor							ashik	0	0	0	0	0	0	0	engineer	amir	155				1	Necessary by internal	0	0		0
3	TWLPune-RS-ML-NCR-2025/003	2025-07-31	16:25:20	0	89	2025-07-31	2025-07-31	2025-07-31	2025-07-31	2026-01-16	2025-07-31	16:30	filter grill is defected	HVAC				Green		TS#03	DMA	HVAC-03	0	0	1	ashik	Defect detected workstation 	location car	Schedule Preventive Maintenance	1		grill material seems to be defective	KSBI		0	1	0	0	\N	\N	WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	WhatsApp Image 2025-06-23 at 3.47.53 PM.jpeg	amir	Mahtab	lead maintainer	Yes	Done	ashik	lead maintainer			Grill 					Supplier		Ashik	0	0	0	0	0	0	0	engineer	Mahtab	169				1	Not necessary	0	0		0
\.


--
-- Data for Name: fracas_ncrids; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_ncrids (uid_id, year, last_id) FROM stdin;
1	2025	3
\.


--
-- Data for Name: fracas_ncrimageslist; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_ncrimageslist (img_id, ncr_gen_id, file_path, is_active) FROM stdin;
1	1	png.png	0
2	2	png.png	0
3	3	png.png	0
4	3	FLOWCHART New Version-Page-3.drawio (1).png	0
5	3	Screenshot 2025-06-19 at 2.00.47 PM (1).png	0
6	1	image 2.jpg	0
\.


--
-- Data for Name: fracas_pbsmaster; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_pbsmaster (id, system, subsystem, product_id, product_description, asset_type, asset_description, "MTBF", "MTBSAF", "MART", asset_quantity, "MTTR", is_active, project_id, availability_target) FROM stdin;
366	Air supply system and Friction Brake System.	Brake Control Equipment	PI0035	Brake Control Equipment	Brakeloop1	Brakeloop refers to the circuit or wiring system that connects various braking components of the train to enable communication, control, and activation of the brake systems.	575	575	0	34	93	0	10	99
367	Air supply system and Friction Brake System.	Brake Control Equipment	PI0036	Brake Control Equipment	Brakeloop3	Brakeloop refers to the circuit or wiring system that connects various braking components of the train to enable communication, control, and activation of the brake systems.	575	575	0	34	93	0	10	99
368	Air supply system and Friction Brake System.	Brake Control Equipment	PI0037	Brake Control Equipment	Breaker Loop	Brakeloop refers to the circuit or wiring system that connects various braking components of the train to enable communication, control, and activation of the brake systems.	575	575	0	34	93	0	10	99
369	Air supply system and Friction Brake System.	Brake Control Equipment	PI0038	Brake Control Equipment	Braking	Collection of components, systems, and devices responsible for slowing down, stopping, or controlling the speed of the train.	575	575	0	34	93	0	10	99
370	Air supply system and Friction Brake System.	Brake Control Equipment	PI0039	Brake Control Equipment	Braking Train Line	Refers to the pneumatic air brake system used to control the application of brakes across multiple cars in a train	575	575	0	34	93	0	10	99
371	Air supply system and Friction Brake System.	Auxiliary Air Supply Equipment	PI0040	Auxiliary Air Supply Equipment	Compressor	Compressor used for train’s operation, powering everything from the braking system to HVAC and pneumatic controls.	575	575	0	34	93	0	10	99
372	Air supply system and Friction Brake System.	Wheel-Side Protection Equipment	PI0041	Wheel-Side Protection Equipment	Slip Slide	Wheel protection equipment	575	575	0	34	93	0	10	99
373	Air supply system and Friction Brake System.	Brake Control Equipment	PI0059	Brake Control Equipment	Brakerloop5	Brakeloop refers to the circuit or wiring system that connects various braking components of the train to enable communication, control, and activation of the brake systems.	575	575	0	34	93	0	10	99
374	Air supply system and Friction Brake System.	Auxiliary Air Supply Equipment	PI0065	Auxiliary Air Supply Equipment	Main Compressor	Compressor used for train’s operation, powering everything from the braking system to HVAC and pneumatic controls.	575	575	0	34	93	0	10	99
375	Air supply system and Friction Brake System.	Auxiliary Air Supply Equipment	PI0066	Auxiliary Air Supply Equipment	Main Compressor/Air Dryer	Compressor used for train’s operation, powering everything from the braking system to HVAC and pneumatic controls.	575	575	0	34	93	0	10	99
376	Air supply system and Friction Brake System.	Wheel-Side Protection Equipment	PI0072	Wheel-Side Protection Equipment	Wheel Slip Slide	Wheel protection equipment	575	575	0	34	93	0	10	99
352	Auxiliary supply system	LVPS 96,0V HNCS 130 XR2 METRO PUNE BATTERY BOX	PI0006	LVPS 96,0V HNCS 130 XR2 METRO PUNE BATTERY BOX	Battery	Batteries crucial components that provide backup power, ensure reliable operation, and maintain safety systems in case of power failure or fluctuations.	1054	1054	0	34	72	0	10	99
350	Wayside Signalling Equipment	Point Machine	PM_Track Eqp	Track Side Equipment for Point Machine	PM_Track	Track Side Equipment for Point Machine	12552302	0	0	360	0	1	1	98
351	Wayside Signalling Equipment	Point Machine	PM_Mechanical Linkage	Mechanical linkages associated with point m/c	PM_Mechanical Linkage	Mechanical linkages associated with point m/c	12552302	0	0	360	0	1	1	98
353	PSS	PSS	UPS	To provides uninterrupted power to the signalling equipment from the main power supply and from battery in the absence of main power supply	UPS	To provides uninterrupted power to the signalling equipment from the main power supply and from battery in the absence of main power supply	125000	0	0	69	0	1	1	98
354	PSS	PSS	SCVS	To protect the equipment damage due to voltage fluctuation	SCVS	To protect the equipment damage due to voltage fluctuation	1	0	0	69	0	1	1	98
355	PSS	PSS	AT	Transformer power supply	AT	Transformer power supply	125000	0	0	69	0	1	1	98
356	MSDAC	MSDAC	Other	Other items	Other	Other items	500	0	0	1331	0	1	1	0
357	MSDAC	Indoor Equipment	ABP	Axle Counter Back Plane	ABP	Axle Counter Back Plane	1704	0	0	1134	0	1	1	0
358	MSDAC	Indoor Equipment	ACB	Axle Counting Board	ACB	Axle Counting Board	624	0	0	1134	0	1	1	0
359	MSDAC	Indoor Equipment	AEB	Adavanced Evaluation Board	AEB	Adavanced Evaluation Board	432	0	0	1331	0	1	1	0
360	MSDAC	Indoor Equipment	COM Card	Communication Board	COM Card	Communication Board	500	0	0	1331	0	1	1	0
361	MSDAC	Track Side Equipment	RSR180	Wheel Sensor	RSR180	Wheel Sensor	3144	0	0	1331	0	1	1	0
362	PSS	PSS	SCVS 	To protect the equipment damage due to voltage fluctuation	SCVS 	To protect the equipment damage due to voltage fluctuation	1	0	0	69	0	1	1	98
363	PSS	PSS	Other 	Items integrating from other subsystems	PSS-Other	Items integrating from other subsystems	1	0	0	69	0	1	1	0
364	Air supply system and Friction Brake System.	Air Suspension Equipment	PI0001	Air Suspension Equipment	Air Dryer	An air dryer in trains is an essential component of the trains pneumatic system, responsible for removing moisture and water vapor from compressed air.	874	874	0	4	93	0	10	99
365	Air supply system and Friction Brake System.	Brake Control Equipment	PI0007	Brake Control Equipment	BECU	The Braking Energy Control Unit (BECU) is a component in some modern train braking systems that controls how braking energy is handled during the deceleration phase.	575	575	0	2	93	0	10	99
377	Auxiliary supply system	Auxiliary Power Supply Box	PI0048	Auxiliary Power Supply Box	APS-1	An APS Box (Auxiliary Power Supply Box) is an important electrical component in modern trains and rail systems. It is responsible for housing the equipment that manages and distributes power to the auxiliary systems on the train.	1054	1054	0	34	72	0	10	99
378	Auxiliary supply system	Auxiliary Power Supply Box	PI0049	Auxiliary Power Supply Box	APS-2	An APS Box (Auxiliary Power Supply Box) is an important electrical component in modern trains and rail systems. It is responsible for housing the equipment that manages and distributes power to the auxiliary systems on the train.	1054	1054	0	34	72	0	10	99
379	Bogie system	Bogie	PI0010	Bogie	Bogie-1	A bogie is essentially a wheelset or axle set mounted on a frame that is connected to the train's carbody (the main structure of the train).	11471	11471	0	1	108	0	10	99
380	Bogie system	Wheel Flange Lubrication System (WFLS)	PI0011	Wheel Flange Lubrication System (WFLS)	WFL	The Wheel Frame Liner is a component used in the wheel or axle assembly of trains	6438	6438	0	34	108	0	10	99
381	Bogie system	WHEEL	PI0012	WHEEL	Wheel	Wheel provide the means for the train to move along the tracks.	6438	6438	0	34	108	0	10	99
382	Bogie system	Wheel/Motor	PI0013	Wheel/Motor	Wheel/Motor	Wheel provide the means for the train to move along the tracks.	6438	6438	0	34	108	0	10	99
383	Communication System	CCTV System	PI0002	CCTV System	3E Camera	Surveillance camera for safety, monitoring and incident detection.	585	585	0	34	49.8	0	10	99
384	Communication System	CCTV System	PI0003	CCTV System	Camera 1F	Used for video surveillance and monitoring systems to improve train operation safety, security, and maintenance.	585	585	0	34	49.8	0	10	99
385	Communication System	CCTV System	PI0004	CCTV System	CCTV	Device used for security surveillance and passenger monitoring. These cameras help improve safety by monitoring both the interior and exterior of the train.	585	585	0	34	49.8	0	10	99
386	Communication System	CCTV System	PI0005	CCTV System	Camera	Used for video surveillance and monitoring systems to improve train operation safety, security, and maintenance.	585	585	0	34	49.8	0	10	99
387	Communication System	Vehicle Control Relay/Contactor/Switch	PI0008	Vehicle Control Relay/Contactor/Switch	ATP	Automatic Train Protection System	585	585	0	34	49.8	0	10	99
388	Pantograph	Pantograph	PI0073	Pantograph	Pantograph	Mechanical device used to collect electricity from the overhead catenary (power) wires and deliver it to the train’s electric traction system.	42000	42000	0	1	90	0	10	99
389	HVAC system and control	HVAC Unit	PI0014	HVAC Unit	Unit-1	Refers to the door located on the left side of the driver's cab or locomotive cabin.	1554	1554	0	1	116.4	0	10	99
390	HVAC system and control	HVAC Unit	PI0015	HVAC Unit	Unit-2	Refers to the door located on the left side of the driver's cab or locomotive cabin.	1554	1554	0	1	116.4	0	10	99
391	HVAC system and control	Vehicle Control Relay/Contactor/Switch	PI0016	Vehicle Control Relay/Contactor/Switch	VDU	Refers to a Vehicle Control Center or Vehicle Control Console, which is a key part of the train's control and monitoring systems.	1554	1554	0	1	116.4	0	10	99
392	HVAC system and control	Vehicle Control Relay/Contactor/Switch	PI0017	Vehicle Control Relay/Contactor/Switch	VCC	Refers to a Vehicle Control Center or Vehicle Control Console, which is a key part of the train's control and monitoring systems.	1554	1554	0	1	116.4	0	10	99
393	Propulsion system	Traction	PI0018	Traction	Traction	refers to the force that propels a train forward and allows it to move along the tracks.	603	603	0	34	97.8	0	10	99
394	Propulsion system	Traction / motor	PI0019	Traction / motor	MOTOR/TRACTION	Refers to the system or process that propels a train. It involves the components and technologies used to generate the power required to move the train, whether it's powered by electricity, diesel, or other means.	1074	1074	0	1	97.8	0	10	99
395	TCMS	Central Control Unit	PI0020	Central Control Unit	TCMS	Train control monitoring system	729	729	0	34	30	0	10	99
396	Communication System	PIS system	PI0021	PIS system	SDU	Side Display Unit	585	585	0	34	49.8	0	10	99
397	Communication System	PIS system	PI0022	PIS system	SLCD	Saloon Liquid Crystal Display (SLCD)	585	585	0	34	49.8	0	10	99
398	Communication System	PIS system	PI0023	PIS system	SDU,SCU	Side Display Unit, Saloon Control Unit	585	585	0	34	49.8	0	10	99
399	Communication System	Vehicle Control MCB & Fuse	PI0024	Vehicle Control MCB & Fuse	PIS-TR	Refers to a Passenger Information System (PIS) for Trains. It is an advanced system that provides real-time information to passengers in a train network, ensuring better communication, comfort, and safety during the journey.	585	585	0	34	49.8	0	10	99
400	Door system, component and control	Left door panel	PI0025	Left door panel	Left Cab Door	Refers to the door located on the left side of the driver's cab or locomotive cabin.	476	476	0	1	47.4	0	10	99
401	Door system, component and control	Door locked switch 2(S2.1)	PI0026	Door locked switch 2(S2.1)	Left Close Push Button	Refers to a button typically located on the left side of a train's door or cab, which, when pressed, closes the door or initiates a sequence to close it.	476	476	0	1	47.4	0	10	99
402	Door system, component and control	Emergency Door	PI0027	Emergency Door	Emergency Door	An Emergency Door in a train is a specially designed door that allows for quick and safe evacuation of passengers in the event of an emergency.	267	267	0	34	47.4	0	10	99
403	Door system, component and control	Driver's Cab Door	PI0028	Driver's Cab Door	Cab Door	Refers to the door that provides access to the train driver's cabin (or locomotive cab).	476	476	0	1	47.4	0	10	99
404	Door system, component and control	Saloon Door	PI0029	Saloon Door	Partition Door	Refers to a door or set of doors used to separate different compartments or sections of a train, creating defined spaces for different purposes	267	267	0	34	47.4	0	10	99
405	Door system, component and control	Saloon Door	PI0030	Saloon Door	EB Push Button	Refers to an Emergency Brake Push Button. This is a safety feature used to manually trigger the emergency braking system of a train.	267	267	0	34	47.4	0	10	99
406	Door system, component and control	Saloon Door	PI0031	Saloon Door	Car Door	Refers to the doors between the passenger cars of a train, or between the train’s compartments.	267	267	0	34	47.4	0	10	99
407	Door system, component and control	Saloon Door	PI0032	Saloon Door	Saloon Door	refers to a type of door that is typically used to separate different compartments or sections within a train, or to provide access to certain areas such as the restroom, crew cabin, or lounge.	267	267	0	34	47.4	0	10	99
408	Door system, component and control	Saloon Door	PI0033	Saloon Door	R4 Door	refers to a type of door that is typically used to separate different compartments or sections within a train, or to provide access to certain areas such as the restroom, crew cabin, or lounge.	267	267	0	34	47.4	0	10	99
409	Door system, component and control	Emergency Door	PI0034	Emergency Door	Rubber Gasket	Rubber gaskets play a crucial role in ensuring the safety, comfort, and efficiency of the train's operation.	476	476	0	1	47.4	0	10	99
410	Door system, component and control	Saloon Door	PI0042	Saloon Door	Cubical 2 Door	Refers to a type of train compartment or carriage configuration where the car has two doors positioned on either side of the compartment.	267	267	0	34	47.4	0	10	99
411	Communication System	Vehicle Control Relay/Contactor/Switch	PI0043	Vehicle Control Relay/Contactor/Switch	ADCL	Automatic Door Control Logic (ADCL) system, helps monitor and provide feedback on the status of the train doors and their control system.	585	585	0	34	49.8	0	10	99
412	Communication System	PIS System	PI0044	PIS System	CI & BECU	Condition Indicator for monitoring the health of train components	585	585	0	34	49.8	0	10	99
413	Communication System	PIS System	PI0045	PIS System	CI-1	Condition Indicator for monitoring the health of train components	585	585	0	34	49.8	0	10	99
414	Communication System	PIS System	PI0046	PIS System	CI-2	Condition Indicator for monitoring the health of train components	585	585	0	34	49.8	0	10	99
415	Communication System	PIS System	PI0047	PIS System	Announcement	Announcements in trains are an essential part of passenger communication, ensuring that travelers are informed about their journey, station stops, safety protocols, and any emergencies.	585	585	0	34	49.8	0	10	99
416	Communication System	Vehicle Control Relay/Contactor/Switch	PI0050	Vehicle Control Relay/Contactor/Switch	Driver Console Button	Refers to the control panel or driver's desk where the train operator interacts with the train's systems to operate it safely and efficiently.	890	890	0	1	49.8	0	10	99
417	Communication System	PIS System	PI0051	PIS System	DRM	Dynamic Route map	585	585	0	34	49.8	0	10	99
418	Door system, component and control	Saloon Door	PI0052	Saloon Door	DCU	Door Control Unit	267	267	0	34	47.4	0	10	99
419	HVAC system and control	HVAC Unit	PI0053	HVAC Unit	HVAC Unit-2	Refers to the door located on the left side of the driver's cab or locomotive cabin.	1554	1554	0	1	116.4	0	10	99
420	HVAC system and control	HVAC Unit	PI0054	HVAC Unit	HVAC Unit-1	Refers to the system that regulates and maintains a comfortable and safe environmental climate within the train.	872	872	0	34	116.4	0	10	99
421	HVAC system and control	HVAC Unit	PI0055	HVAC Unit	HVAC	Refers to the system that regulates and maintains a comfortable and safe environmental climate within the train.	872	872	0	34	116.4	0	10	99
422	Light System	Interior Lightning	PI0056	Interior Lightning	Lighting	Interior Lightning	3217	3217	0	34	18	0	10	99
423	Light System	External Lighting	PI0057	External Lighting	Head Light	Component for illuminating the track ahead of the train and make the train visible to other rail vehicles and signal systems.	3217	3217	0	34	18	0	10	99
424	Door system, component and control	wiper system	PI0058	wiper system	Wiper	refers to the windshield wiper or train window wiper system that is used to clear rain, snow, dirt, and debris from the windows or windshields.	267	267	0	34	47.4	0	10	99
425	Communication System	CCTV System	PI0060	PIS System	ER	Emergency Radio	585	585	0	34	49.8	0	10	99
426	Propulsion system	Traction	PI0061	Traction	FDU	The FDU (Field Diagnostic Unit) plays a critical role in ensuring the optimal performance of a train's propulsion system.	1074	1074	0	1	97.8	0	10	99
427	Communication System	CCTV System	PI0062	PIS System	ER/VDU	Video Display Unit	585	585	0	34	49.8	0	10	99
428	Communication System	CCTV System	PI0063	CCTV System	MDS/CCTV	Refers to an integrated system used for monitoring, diagnosing, and troubleshooting various subsystems of a train.	585	585	0	34	49.8	0	10	99
429	Communication System	CCTV System	PI0064	CCTV System	MDS	Refers to an integrated system used for monitoring, diagnosing, and troubleshooting various subsystems of a train.	585	585	0	34	49.8	0	10	99
430	Communication System	PIS System	PI0067	PIS System	MOP/PTT	Main Operational Pannel	585	585	0	34	49.8	0	10	99
431	Light System	External Lighting	PI0068	External Lighting	Marker Light	External Light	3217	3217	0	34	18	0	10	99
432	Communication System	Vehicle Control MCB & Fuse	PI0069	Vehicle Control MCB & Fuse	PA	Refers to a Passenger Information System (PIS) for Trains. It is an advanced system that provides real-time information to passengers in a train network, ensuring better communication, comfort, and safety during the journey.	585	585	0	34	49.8	0	10	99
433	Communication System	Vehicle Control MCB & Fuse	PI0070	Vehicle Control MCB & Fuse	PA/PIS	Refers to a Passenger Information System (PIS) for Trains. It is an advanced system that provides real-time information to passengers in a train network, ensuring better communication, comfort, and safety during the journey.	585	585	0	34	49.8	0	10	99
434	Traction Motor	Traction / motor	PI0074	Traction / motor	Traction Motor	traction motor is a crucial component in electric trains, used to provide the power needed for the train to move.	264706	264706	0	1	120	0	10	99
349	Wayside Signalling Equipment	Point Machine	PM_Gear Drive	unlocking & operating the point switches in the desired position  lock them  detect their correct setting with the aid of an electric motor	PM-Gear Drive	unlocking  operating the point switches in the desired position  lock them  detect their correct setting with the aid of an electric motor	12552301	0	0	360	0	1	1	98
\.


--
-- Data for Name: fracas_pbsunit; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_pbsunit (id, "MTBFMTBSAF", "MTTR", average_speed, chk_average_speed, num_of_days, running_time) FROM stdin;
3	hrs	hrs	34	1	7	20
\.


--
-- Data for Name: fracas_product; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_product (product_id, product_name, description, "MTBF", "MTBSAF", "MTTR", availability_target, is_active, num_of_trains) FROM stdin;
5	ddddddddd11		222	222	222	2222	1	0
4	ddddddddd		111	111	111	111	1	0
6	tvs		222	222	222	34	1	0
7	tvshh		55	55	55	55	1	0
8	tvs1		100	100	100	10	1	0
3	Telecom	Telecom	100	100	100	90	0	0
2	P5A-TPWS	P5A-TPWS	100	100	100	95.5	0	0
9	test		0.001	0.001	-0.001	0.001	1	0
1	P5-Signalling	P5-Signalling	20000	168	100	99	0	0
10	PuneMetro		2941.176	2941.176	62	99.33	0	34
\.


--
-- Data for Name: fracas_reviewboard; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_reviewboard (id, asset_type, meeting_date, meeting_id, from_date, to_date, meeting_status, meeting_outcome, "P_id", is_active) FROM stdin;
82	414	2025-07-17	\N	2024-08-01	2024-09-30			10	0
83	378	2025-07-18	\N	2025-07-09	2025-07-09			10	1
\.


--
-- Data for Name: fracas_rootcause; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_rootcause (root_cause_id, root_cause_description, rca_workshop_date, root_cause_status, defect_id, asset_type, immediate_cause, leading_reasons, "P_id", is_active, material_is_damaged, organistaional_management_cause, systemic_cause, assembly_no, failure_detection) FROM stdin;
87	root cause description 	2025-06-12	Open	189	414	immediate cause	leading reason	10	0	Yes	organizational/management cause 	systemic cause		
88	quality of rubber was not as per the standards. 	2025-07-29	Open	191	421	bearing deffective	rubber material was deffective	10	0	Yes				
89	quality seems to be poor of the material used in grill	2025-07-31	Open	192	421	due to bad air quality	extensively usage of air filter	10	0	Yes				
90	*Root cause description (3rd Why)	2025-07-17	Open	193	421	*Immediate cause (1st Why):	*Leading reasons (2nd Why):	10	0	Yes				TS
\.


--
-- Data for Name: fracas_systems; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_systems (id, "System", "MTBF", "MTBSAF", "MTTR", availability_target, is_active, project_id) FROM stdin;
1	PSS	90	90	90	90	0	1
2	Air supply system and Friction Brake System.	575	575	93	99.9	0	10
\.


--
-- Data for Name: fracas_temp_table_asset_register; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_temp_table_asset_register (id, asset_config_id, asset_serial_number, location_id, location_description, asset_type, asset_type_id, software_version, asset_description, software_description, asset_status, is_active, "P_id", error_list, updated_by) FROM stdin;
\.


--
-- Data for Name: fracas_temp_table_failure_data; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_temp_table_failure_data (id, failure_id, asset_type, asset_config_id, asset_type_id, event_description, mode_id, date, "time", detection, service_delay, immediate_investigation, failure_type, safety_failure, hazard_id, cm_description, replaced_asset_config_id, cm_start_date, cm_start_time, cm_end_date, cm_end_time, oem_failure_reference, defect, error_list, "P_id", updated_by) FROM stdin;
\.


--
-- Data for Name: fracas_temp_table_failure_mode; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_temp_table_failure_mode (id, mode_id, mode_description, asset_type, asset_type_id, "P_id", updated_by, error_list) FROM stdin;
\.


--
-- Data for Name: fracas_temp_table_failuredata; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_temp_table_failuredata (id, asset_type, failure_id, asset_config_id, event_description, mode_id, mode_description, date, "time", detection, service_delay, immediate_investigation, failure_type, safety_failure, hazard_id, cm_description, replaced_asset_config_id, cm_start_date, cm_start_time, cm_end_date, cm_end_time, oem_failure_reference, defect, "P_id", is_active, updated_by) FROM stdin;
\.


--
-- Data for Name: fracas_temp_table_import_file; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_temp_table_import_file (id, system, subsystem, subsystem_id, product_id, product_description, asset_type, asset_description, "MTBF", "MTBSAF", "MTTR", "MART", asset_quantity, error_list, updated_by) FROM stdin;
\.


--
-- Data for Name: fracas_userprofile; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_userprofile (id, first_name, last_name, created_at, updated_at, user_id, product_id_id, user_role_id, is_active, is_disable) FROM stdin;
14	Admin	Admin	2021-11-29 04:52:54.911948+00	2021-11-29 04:52:54.911948+00	28	1	1	0	0
16	Tom	Tom	2021-11-29 06:15:17.484988+00	2021-11-29 06:15:17.484988+00	30	3	2	0	0
17	Jerrry	Jerrry	2021-11-29 06:15:37.077615+00	2021-11-29 06:15:37.077615+00	31	3	4	0	0
18	Suhu	Suhu	2021-11-29 06:16:00.510131+00	2021-11-29 06:16:00.510131+00	32	1	2	0	0
19	John	Doe	2021-11-29 06:16:36.587684+00	2021-11-29 06:16:36.587684+00	33	3	2	0	0
20	John	Smith	2021-11-29 06:17:09.715727+00	2021-11-29 06:17:09.715727+00	34	3	3	0	0
21	Super	Admin	2021-12-17 07:41:50.547333+00	2021-12-17 07:41:50.547333+00	35	1	1	0	0
15	Gabriel	Gabriel	2021-11-29 06:14:49.007624+00	2021-11-29 06:14:49.007624+00	29	1	3	0	0
23	Intellex	Testing	2022-01-10 04:38:33.129335+00	2022-01-10 04:38:33.129352+00	37	2	3	0	0
22	omkar	ka	2022-01-08 07:05:38.736322+00	2022-01-08 07:05:38.736352+00	36	2	3	0	0
24	SAM	JOHN	2022-01-19 10:08:18.566361+00	2022-01-19 10:08:18.56638+00	38	1	4	0	0
25	Operator	PPIO	2025-07-03 06:03:57.111783+00	2025-07-03 06:03:57.111799+00	39	10	5	0	0
26	Maintainer	Titagarh	2025-07-03 06:05:37.573602+00	2025-07-03 06:05:37.573615+00	40	10	6	0	0
27	RAM	Engineer	2025-07-03 06:07:52.733624+00	2025-07-03 06:07:52.733637+00	41	10	3	0	0
28	Admin	Level	2025-07-03 06:09:41.590605+00	2025-07-03 06:09:41.590618+00	42	10	2	0	0
29	View	Level	2025-07-03 06:10:05.3008+00	2025-07-03 06:10:05.300815+00	43	10	4	0	0
30	Rajkumar	Anumula	2025-08-01 08:38:36.118826+00	2025-08-01 08:38:36.11884+00	44	10	6	0	0
31	Mahendra Singh	Jadaun	2025-08-01 08:43:51.61874+00	2025-08-01 08:43:51.618753+00	45	10	6	0	0
32	Sandeep Narayan	Jadhav	2025-08-01 08:46:34.036068+00	2025-08-01 08:46:34.036082+00	46	10	6	0	0
33	Narayan Prasad	Verma	2025-08-01 08:48:24.259758+00	2025-08-01 08:48:24.259775+00	47	10	6	0	0
34	Abhishek	Verma	2025-08-01 08:50:10.434305+00	2025-08-01 08:50:10.434321+00	48	10	6	0	0
35	Ramesh	Bhukya	2025-08-01 08:52:28.020758+00	2025-08-01 08:52:28.020773+00	49	10	6	0	0
36	Mahtab 	Alam	2025-08-02 08:14:44.902166+00	2025-08-02 08:14:44.902185+00	50	10	7	0	0
\.


--
-- Data for Name: fracas_userresetkey; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fracas_userresetkey (id, key, expires_on, otp_expires_on, date, user_id) FROM stdin;
\.


--
-- Name: admin_tools_stats_criteriatostatsm2m_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.admin_tools_stats_criteriatostatsm2m_id_seq', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 192, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 50, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: dash_stats_criteria_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dash_stats_criteria_id_seq', 1, false);


--
-- Name: dashboard_stats_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_stats_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 4254, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 48, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 215, true);


--
-- Name: fracas_action_action_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_action_action_id_seq', 35, true);


--
-- Name: fracas_asset_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_asset_id_seq', 2009, true);


--
-- Name: fracas_assetregister_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_assetregister_id_seq', 1, false);


--
-- Name: fracas_assetserialnumberids_uid_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_assetserialnumberids_uid_id_seq', 1, false);


--
-- Name: fracas_correctiveaction_corrective_action_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_correctiveaction_corrective_action_id_seq', 131, true);


--
-- Name: fracas_defect_defect_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_defect_defect_id_seq', 194, true);


--
-- Name: fracas_defectdiscussion_attendees_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_defectdiscussion_attendees_id_seq', 67, true);


--
-- Name: fracas_defectdiscussion_defect_discussion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_defectdiscussion_defect_discussion_id_seq', 80, true);


--
-- Name: fracas_eirids_uid_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_eirids_uid_id_seq', 1, true);


--
-- Name: fracas_eirimages_img_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_eirimages_img_id_seq', 4, true);


--
-- Name: fracas_employeemaster_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_employeemaster_id_seq', 16, true);


--
-- Name: fracas_failuredata_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_failuredata_id_seq', 28806, true);


--
-- Name: fracas_failuredataids_uid_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_failuredataids_uid_id_seq', 2, true);


--
-- Name: fracas_failuremode_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_failuremode_id_seq', 2072, true);


--
-- Name: fracas_history_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_history_id_seq', 1533, true);


--
-- Name: fracas_investigationdetails_details_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_investigationdetails_details_id_seq', 2, true);


--
-- Name: fracas_jobcard_job_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_jobcard_job_id_seq', 62, true);


--
-- Name: fracas_jobcardids_uid_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_jobcardids_uid_id_seq', 2, true);


--
-- Name: fracas_jobdetails_job_details_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_jobdetails_job_details_id_seq', 12, true);


--
-- Name: fracas_jobreplacedequipment_job_equipment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_jobreplacedequipment_job_equipment_id_seq', 1, true);


--
-- Name: fracas_jobworktomaintainers_job_work_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_jobworktomaintainers_job_work_id_seq', 9, true);


--
-- Name: fracas_kilometrereading_km_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_kilometrereading_km_id_seq', 20, true);


--
-- Name: fracas_ncrgeneration_rec_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_ncrgeneration_rec_id_seq', 3, true);


--
-- Name: fracas_ncrids_uid_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_ncrids_uid_id_seq', 1, true);


--
-- Name: fracas_ncrimageslist_img_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_ncrimageslist_img_id_seq', 6, true);


--
-- Name: fracas_pbsmaster_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_pbsmaster_id_seq', 434, true);


--
-- Name: fracas_pbsunit_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_pbsunit_id_seq', 3, true);


--
-- Name: fracas_product_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_product_product_id_seq', 10, true);


--
-- Name: fracas_reviewboard_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_reviewboard_id_seq', 83, true);


--
-- Name: fracas_rirgeneration_eir_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_rirgeneration_eir_id_seq', 60, true);


--
-- Name: fracas_rootcause_root_cause_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_rootcause_root_cause_id_seq', 90, true);


--
-- Name: fracas_systems_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_systems_id_seq', 2, true);


--
-- Name: fracas_temp_table_asset_register_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_temp_table_asset_register_id_seq', 198, true);


--
-- Name: fracas_temp_table_failure_data_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_temp_table_failure_data_id_seq', 1675, true);


--
-- Name: fracas_temp_table_failure_mode_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_temp_table_failure_mode_id_seq', 14, true);


--
-- Name: fracas_temp_table_failuredata_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_temp_table_failuredata_id_seq', 1, false);


--
-- Name: fracas_temp_table_import_file_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_temp_table_import_file_id_seq', 23, true);


--
-- Name: fracas_userprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_userprofile_id_seq', 36, true);


--
-- Name: fracas_userresetkey_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fracas_userresetkey_id_seq', 1, false);


--
-- Name: admin_tools_stats_criteriatostatsm2m admin_tools_stats_criteriatostatsm2m_order_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin_tools_stats_criteriatostatsm2m
    ADD CONSTRAINT admin_tools_stats_criteriatostatsm2m_order_key UNIQUE ("order");


--
-- Name: admin_tools_stats_criteriatostatsm2m admin_tools_stats_criteriatostatsm2m_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin_tools_stats_criteriatostatsm2m
    ADD CONSTRAINT admin_tools_stats_criteriatostatsm2m_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: dash_stats_criteria dash_stats_criteria_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dash_stats_criteria
    ADD CONSTRAINT dash_stats_criteria_pkey PRIMARY KEY (id);


--
-- Name: dashboard_stats dashboard_stats_graph_key_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_stats
    ADD CONSTRAINT dashboard_stats_graph_key_key UNIQUE (graph_key);


--
-- Name: dashboard_stats dashboard_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_stats
    ADD CONSTRAINT dashboard_stats_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: fracas_action fracas_action_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_action
    ADD CONSTRAINT fracas_action_pkey PRIMARY KEY (action_id);


--
-- Name: fracas_asset fracas_asset_asset_config_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_asset
    ADD CONSTRAINT fracas_asset_asset_config_id_key UNIQUE (asset_config_id);


--
-- Name: fracas_asset fracas_asset_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_asset
    ADD CONSTRAINT fracas_asset_pkey PRIMARY KEY (id);


--
-- Name: fracas_assetregister fracas_assetregister_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_assetregister
    ADD CONSTRAINT fracas_assetregister_pkey PRIMARY KEY (id);


--
-- Name: fracas_assetserialnumberids fracas_assetserialnumberids_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_assetserialnumberids
    ADD CONSTRAINT fracas_assetserialnumberids_pkey PRIMARY KEY (uid_id);


--
-- Name: fracas_correctiveaction fracas_correctiveaction_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_correctiveaction
    ADD CONSTRAINT fracas_correctiveaction_pkey PRIMARY KEY (corrective_action_id);


--
-- Name: fracas_defect fracas_defect_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_defect
    ADD CONSTRAINT fracas_defect_pkey PRIMARY KEY (defect_id);


--
-- Name: fracas_defectdiscussion_attendees fracas_defectdiscussion__defectdiscussion_id_empl_4c58967a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_defectdiscussion_attendees
    ADD CONSTRAINT fracas_defectdiscussion__defectdiscussion_id_empl_4c58967a_uniq UNIQUE (defectdiscussion_id, userprofile_id);


--
-- Name: fracas_defectdiscussion_attendees fracas_defectdiscussion_attendees_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_defectdiscussion_attendees
    ADD CONSTRAINT fracas_defectdiscussion_attendees_pkey PRIMARY KEY (id);


--
-- Name: fracas_defectdiscussion fracas_defectdiscussion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_defectdiscussion
    ADD CONSTRAINT fracas_defectdiscussion_pkey PRIMARY KEY (defect_discussion_id);


--
-- Name: fracas_eirids fracas_eirids_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_eirids
    ADD CONSTRAINT fracas_eirids_pkey PRIMARY KEY (uid_id);


--
-- Name: fracas_eirimages fracas_eirimages_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_eirimages
    ADD CONSTRAINT fracas_eirimages_pkey PRIMARY KEY (img_id);


--
-- Name: fracas_employeemaster fracas_employeemaster_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_employeemaster
    ADD CONSTRAINT fracas_employeemaster_pkey PRIMARY KEY (id);


--
-- Name: fracas_failuredata fracas_failuredata_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_failuredata
    ADD CONSTRAINT fracas_failuredata_pkey PRIMARY KEY (id);


--
-- Name: fracas_failuredataids fracas_failuredataids_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_failuredataids
    ADD CONSTRAINT fracas_failuredataids_pkey PRIMARY KEY (uid_id);


--
-- Name: fracas_failuremode fracas_failuremode_mode_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_failuremode
    ADD CONSTRAINT fracas_failuremode_mode_id_key UNIQUE (mode_id);


--
-- Name: fracas_failuremode fracas_failuremode_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_failuremode
    ADD CONSTRAINT fracas_failuremode_pkey PRIMARY KEY (id);


--
-- Name: fracas_history fracas_history_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_history
    ADD CONSTRAINT fracas_history_pkey PRIMARY KEY (id);


--
-- Name: fracas_investigationdetails fracas_investigationdetails_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_investigationdetails
    ADD CONSTRAINT fracas_investigationdetails_pkey PRIMARY KEY (details_id);


--
-- Name: fracas_jobcard fracas_jobcard_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_jobcard
    ADD CONSTRAINT fracas_jobcard_pkey PRIMARY KEY (job_id);


--
-- Name: fracas_jobcardids fracas_jobcardids_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_jobcardids
    ADD CONSTRAINT fracas_jobcardids_pkey PRIMARY KEY (uid_id);


--
-- Name: fracas_jobdetails fracas_jobdetails_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_jobdetails
    ADD CONSTRAINT fracas_jobdetails_pkey PRIMARY KEY (job_details_id);


--
-- Name: fracas_jobreplacedequipment fracas_jobreplacedequipment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_jobreplacedequipment
    ADD CONSTRAINT fracas_jobreplacedequipment_pkey PRIMARY KEY (job_equipment_id);


--
-- Name: fracas_jobworktomaintainers fracas_jobworktomaintainers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_jobworktomaintainers
    ADD CONSTRAINT fracas_jobworktomaintainers_pkey PRIMARY KEY (job_work_id);


--
-- Name: fracas_kilometrereading fracas_kilometrereading_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_kilometrereading
    ADD CONSTRAINT fracas_kilometrereading_pkey PRIMARY KEY (km_id);


--
-- Name: fracas_ncrgeneration fracas_ncrgeneration_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_ncrgeneration
    ADD CONSTRAINT fracas_ncrgeneration_pkey PRIMARY KEY (rec_id);


--
-- Name: fracas_ncrids fracas_ncrids_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_ncrids
    ADD CONSTRAINT fracas_ncrids_pkey PRIMARY KEY (uid_id);


--
-- Name: fracas_ncrimageslist fracas_ncrimageslist_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_ncrimageslist
    ADD CONSTRAINT fracas_ncrimageslist_pkey PRIMARY KEY (img_id);


--
-- Name: fracas_pbsmaster fracas_pbsmaster_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_pbsmaster
    ADD CONSTRAINT fracas_pbsmaster_pkey PRIMARY KEY (id);


--
-- Name: fracas_pbsunit fracas_pbsunit_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_pbsunit
    ADD CONSTRAINT fracas_pbsunit_pkey PRIMARY KEY (id);


--
-- Name: fracas_product fracas_product_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_product
    ADD CONSTRAINT fracas_product_pkey PRIMARY KEY (product_id);


--
-- Name: fracas_reviewboard fracas_reviewboard_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_reviewboard
    ADD CONSTRAINT fracas_reviewboard_pkey PRIMARY KEY (id);


--
-- Name: fracas_eirgeneration fracas_rirgeneration_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_eirgeneration
    ADD CONSTRAINT fracas_rirgeneration_pkey PRIMARY KEY (eir_id);


--
-- Name: fracas_rootcause fracas_rootcause_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_rootcause
    ADD CONSTRAINT fracas_rootcause_pkey PRIMARY KEY (root_cause_id);


--
-- Name: fracas_systems fracas_systems_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_systems
    ADD CONSTRAINT fracas_systems_pkey PRIMARY KEY (id);


--
-- Name: fracas_temp_table_asset_register fracas_temp_table_asset_register_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_temp_table_asset_register
    ADD CONSTRAINT fracas_temp_table_asset_register_pkey PRIMARY KEY (id);


--
-- Name: fracas_temp_table_failure_data fracas_temp_table_failure_data_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_temp_table_failure_data
    ADD CONSTRAINT fracas_temp_table_failure_data_pkey PRIMARY KEY (id);


--
-- Name: fracas_temp_table_failure_mode fracas_temp_table_failure_mode_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_temp_table_failure_mode
    ADD CONSTRAINT fracas_temp_table_failure_mode_pkey PRIMARY KEY (id);


--
-- Name: fracas_temp_table_failuredata fracas_temp_table_failuredata_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_temp_table_failuredata
    ADD CONSTRAINT fracas_temp_table_failuredata_pkey PRIMARY KEY (id);


--
-- Name: fracas_temp_table_import_file fracas_temp_table_import_file_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_temp_table_import_file
    ADD CONSTRAINT fracas_temp_table_import_file_pkey PRIMARY KEY (id);


--
-- Name: fracas_userprofile fracas_userprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_userprofile
    ADD CONSTRAINT fracas_userprofile_pkey PRIMARY KEY (id);


--
-- Name: fracas_userresetkey fracas_userresetkey_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_userresetkey
    ADD CONSTRAINT fracas_userresetkey_pkey PRIMARY KEY (id);


--
-- Name: admin_tools_stats_criteriatostatsm2m_criteria_id_bfe67f05; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX admin_tools_stats_criteriatostatsm2m_criteria_id_bfe67f05 ON public.admin_tools_stats_criteriatostatsm2m USING btree (criteria_id);


--
-- Name: admin_tools_stats_criteriatostatsm2m_stats_id_10bd79ea; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX admin_tools_stats_criteriatostatsm2m_stats_id_10bd79ea ON public.admin_tools_stats_criteriatostatsm2m USING btree (stats_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: dash_stats_criteria_criteria_name_7fe7ae1e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dash_stats_criteria_criteria_name_7fe7ae1e ON public.dash_stats_criteria USING btree (criteria_name);


--
-- Name: dash_stats_criteria_criteria_name_7fe7ae1e_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dash_stats_criteria_criteria_name_7fe7ae1e_like ON public.dash_stats_criteria USING btree (criteria_name varchar_pattern_ops);


--
-- Name: dashboard_stats_graph_key_4256e63f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dashboard_stats_graph_key_4256e63f_like ON public.dashboard_stats USING btree (graph_key varchar_pattern_ops);


--
-- Name: dashboard_stats_graph_title_99e6d271; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dashboard_stats_graph_title_99e6d271 ON public.dashboard_stats USING btree (graph_title);


--
-- Name: dashboard_stats_graph_title_99e6d271_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dashboard_stats_graph_title_99e6d271_like ON public.dashboard_stats USING btree (graph_title varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: fracas_action_defect_discussion_id_id_22ab6bd9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_action_defect_discussion_id_id_22ab6bd9 ON public.fracas_action USING btree (defect_discussion_id_id);


--
-- Name: fracas_asset_asset_config_id_1b7bf1fc_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_asset_asset_config_id_1b7bf1fc_like ON public.fracas_asset USING btree (asset_config_id varchar_pattern_ops);


--
-- Name: fracas_correctiveaction_defect_id_6b07c98b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_correctiveaction_defect_id_6b07c98b ON public.fracas_correctiveaction USING btree (defect_id);


--
-- Name: fracas_defectdiscussion_attendees_defectdiscussion_id_68582c3b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_defectdiscussion_attendees_defectdiscussion_id_68582c3b ON public.fracas_defectdiscussion_attendees USING btree (defectdiscussion_id);


--
-- Name: fracas_defectdiscussion_attendees_employeemaster_id_97632480; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_defectdiscussion_attendees_employeemaster_id_97632480 ON public.fracas_defectdiscussion_attendees USING btree (userprofile_id);


--
-- Name: fracas_defectdiscussion_defect_id_777a85b9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_defectdiscussion_defect_id_777a85b9 ON public.fracas_defectdiscussion USING btree (defect_id);


--
-- Name: fracas_defectdiscussion_review_board_id_30bd7f7d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_defectdiscussion_review_board_id_30bd7f7d ON public.fracas_defectdiscussion USING btree (review_board_id);


--
-- Name: fracas_eirimages_eir_dt_id_id_a1e83e2d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_eirimages_eir_dt_id_id_a1e83e2d ON public.fracas_eirimages USING btree (eir_dt_id_id);


--
-- Name: fracas_failuredata_asset_config_id_id_411469d0; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_failuredata_asset_config_id_id_411469d0 ON public.fracas_failuredata USING btree (asset_config_id_id);


--
-- Name: fracas_failuredata_asset_config_id_id_411469d0_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_failuredata_asset_config_id_id_411469d0_like ON public.fracas_failuredata USING btree (asset_config_id_id varchar_pattern_ops);


--
-- Name: fracas_failuredata_defect_id_45343e26; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_failuredata_defect_id_45343e26 ON public.fracas_failuredata USING btree (defect_id);


--
-- Name: fracas_failuredata_mode_id_id_32b9227b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_failuredata_mode_id_id_32b9227b ON public.fracas_failuredata USING btree (mode_id_id);


--
-- Name: fracas_failuremode_mode_id_68d1dc4e_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_failuremode_mode_id_68d1dc4e_like ON public.fracas_failuremode USING btree (mode_id varchar_pattern_ops);


--
-- Name: fracas_history_user_id_508829c0; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_history_user_id_508829c0 ON public.fracas_history USING btree (user_id);


--
-- Name: fracas_investigationdetails_eir_dt_id_id_d8fa5478; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_investigationdetails_eir_dt_id_id_d8fa5478 ON public.fracas_investigationdetails USING btree (eir_dt_id_id);


--
-- Name: fracas_jobcard_failure_id_id_18695844; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_jobcard_failure_id_id_18695844 ON public.fracas_jobcard USING btree (failure_id_id);


--
-- Name: fracas_jobdetails_job_card_id_id_9c8ee03f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_jobdetails_job_card_id_id_9c8ee03f ON public.fracas_jobdetails USING btree (job_card_id_id);


--
-- Name: fracas_jobreplacedequipment_job_card_id_id_e434c5bd; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_jobreplacedequipment_job_card_id_id_e434c5bd ON public.fracas_jobreplacedequipment USING btree (job_card_id_id);


--
-- Name: fracas_jobworktomaintainers_job_card_id_id_7cd42e63; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_jobworktomaintainers_job_card_id_id_7cd42e63 ON public.fracas_jobworktomaintainers USING btree (job_card_id_id);


--
-- Name: fracas_ncrgeneration_rootcause_id_id_80ebc6f4; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_ncrgeneration_rootcause_id_id_80ebc6f4 ON public.fracas_ncrgeneration USING btree (rootcause_id_id);


--
-- Name: fracas_pbsmaster_project_id_967c21df; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_pbsmaster_project_id_967c21df ON public.fracas_pbsmaster USING btree (project_id);


--
-- Name: fracas_rirgeneration_failure_id_id_392ffa12; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_rirgeneration_failure_id_id_392ffa12 ON public.fracas_eirgeneration USING btree (failure_id_id);


--
-- Name: fracas_rootcause_defect_id_d3f53143; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_rootcause_defect_id_d3f53143 ON public.fracas_rootcause USING btree (defect_id);


--
-- Name: fracas_systems_project_id_6f83b733; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_systems_project_id_6f83b733 ON public.fracas_systems USING btree (project_id);


--
-- Name: fracas_userprofile_product_id_id_b5877d4c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_userprofile_product_id_id_b5877d4c ON public.fracas_userprofile USING btree (product_id_id);


--
-- Name: fracas_userprofile_user_id_a6d557eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_userprofile_user_id_a6d557eb ON public.fracas_userprofile USING btree (user_id);


--
-- Name: fracas_userprofile_user_type_id_c66bfd15; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_userprofile_user_type_id_c66bfd15 ON public.fracas_userprofile USING btree (user_role_id);


--
-- Name: fracas_userresetkey_key_1d7664f0; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_userresetkey_key_1d7664f0 ON public.fracas_userresetkey USING btree (key);


--
-- Name: fracas_userresetkey_key_1d7664f0_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_userresetkey_key_1d7664f0_like ON public.fracas_userresetkey USING btree (key varchar_pattern_ops);


--
-- Name: fracas_userresetkey_user_id_499fbb9d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fracas_userresetkey_user_id_499fbb9d ON public.fracas_userresetkey USING btree (user_id);


--
-- Name: admin_tools_stats_criteriatostatsm2m admin_tools_stats_cr_criteria_id_bfe67f05_fk_dash_stat; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin_tools_stats_criteriatostatsm2m
    ADD CONSTRAINT admin_tools_stats_cr_criteria_id_bfe67f05_fk_dash_stat FOREIGN KEY (criteria_id) REFERENCES public.dash_stats_criteria(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: admin_tools_stats_criteriatostatsm2m admin_tools_stats_cr_stats_id_10bd79ea_fk_dashboard; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin_tools_stats_criteriatostatsm2m
    ADD CONSTRAINT admin_tools_stats_cr_stats_id_10bd79ea_fk_dashboard FOREIGN KEY (stats_id) REFERENCES public.dashboard_stats(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_action fracas_action_defect_discussion_id_22ab6bd9_fk_fracas_de; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_action
    ADD CONSTRAINT fracas_action_defect_discussion_id_22ab6bd9_fk_fracas_de FOREIGN KEY (defect_discussion_id_id) REFERENCES public.fracas_defectdiscussion(defect_discussion_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_correctiveaction fracas_correctiveact_defect_id_6b07c98b_fk_fracas_de; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_correctiveaction
    ADD CONSTRAINT fracas_correctiveact_defect_id_6b07c98b_fk_fracas_de FOREIGN KEY (defect_id) REFERENCES public.fracas_defect(defect_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_defectdiscussion fracas_defectdiscuss_defect_id_777a85b9_fk_fracas_de; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_defectdiscussion
    ADD CONSTRAINT fracas_defectdiscuss_defect_id_777a85b9_fk_fracas_de FOREIGN KEY (defect_id) REFERENCES public.fracas_defect(defect_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_defectdiscussion_attendees fracas_defectdiscuss_defectdiscussion_id_68582c3b_fk_fracas_de; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_defectdiscussion_attendees
    ADD CONSTRAINT fracas_defectdiscuss_defectdiscussion_id_68582c3b_fk_fracas_de FOREIGN KEY (defectdiscussion_id) REFERENCES public.fracas_defectdiscussion(defect_discussion_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_defectdiscussion fracas_defectdiscuss_review_board_id_30bd7f7d_fk_fracas_re; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_defectdiscussion
    ADD CONSTRAINT fracas_defectdiscuss_review_board_id_30bd7f7d_fk_fracas_re FOREIGN KEY (review_board_id) REFERENCES public.fracas_reviewboard(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_defectdiscussion_attendees fracas_defectdiscuss_userprofile_id_40c62480_fk_fracas_us; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_defectdiscussion_attendees
    ADD CONSTRAINT fracas_defectdiscuss_userprofile_id_40c62480_fk_fracas_us FOREIGN KEY (userprofile_id) REFERENCES public.fracas_userprofile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_eirimages fracas_eirimages_eir_dt_id_id_a1e83e2d_fk_fracas_ei; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_eirimages
    ADD CONSTRAINT fracas_eirimages_eir_dt_id_id_a1e83e2d_fk_fracas_ei FOREIGN KEY (eir_dt_id_id) REFERENCES public.fracas_eirgeneration(eir_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_failuredata fracas_failuredata_asset_config_id_id_411469d0_fk_fracas_as; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_failuredata
    ADD CONSTRAINT fracas_failuredata_asset_config_id_id_411469d0_fk_fracas_as FOREIGN KEY (asset_config_id_id) REFERENCES public.fracas_asset(asset_config_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_failuredata fracas_failuredata_defect_id_45343e26_fk_fracas_de; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_failuredata
    ADD CONSTRAINT fracas_failuredata_defect_id_45343e26_fk_fracas_de FOREIGN KEY (defect_id) REFERENCES public.fracas_defect(defect_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_failuredata fracas_failuredata_mode_id_id_32b9227b_fk_fracas_failuremode_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_failuredata
    ADD CONSTRAINT fracas_failuredata_mode_id_id_32b9227b_fk_fracas_failuremode_id FOREIGN KEY (mode_id_id) REFERENCES public.fracas_failuremode(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_history fracas_history_user_id_508829c0_fk_fracas_userprofile_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_history
    ADD CONSTRAINT fracas_history_user_id_508829c0_fk_fracas_userprofile_id FOREIGN KEY (user_id) REFERENCES public.fracas_userprofile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_investigationdetails fracas_investigation_eir_dt_id_id_d8fa5478_fk_fracas_ei; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_investigationdetails
    ADD CONSTRAINT fracas_investigation_eir_dt_id_id_d8fa5478_fk_fracas_ei FOREIGN KEY (eir_dt_id_id) REFERENCES public.fracas_eirgeneration(eir_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_jobcard fracas_jobcard_failure_id_id_18695844_fk_fracas_failuredata_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_jobcard
    ADD CONSTRAINT fracas_jobcard_failure_id_id_18695844_fk_fracas_failuredata_id FOREIGN KEY (failure_id_id) REFERENCES public.fracas_failuredata(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_jobdetails fracas_jobdetails_job_card_id_id_9c8ee03f_fk_fracas_jo; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_jobdetails
    ADD CONSTRAINT fracas_jobdetails_job_card_id_id_9c8ee03f_fk_fracas_jo FOREIGN KEY (job_card_id_id) REFERENCES public.fracas_jobcard(job_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_jobreplacedequipment fracas_jobreplacedeq_job_card_id_id_e434c5bd_fk_fracas_jo; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_jobreplacedequipment
    ADD CONSTRAINT fracas_jobreplacedeq_job_card_id_id_e434c5bd_fk_fracas_jo FOREIGN KEY (job_card_id_id) REFERENCES public.fracas_jobcard(job_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_jobworktomaintainers fracas_jobworktomain_job_card_id_id_7cd42e63_fk_fracas_jo; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_jobworktomaintainers
    ADD CONSTRAINT fracas_jobworktomain_job_card_id_id_7cd42e63_fk_fracas_jo FOREIGN KEY (job_card_id_id) REFERENCES public.fracas_jobcard(job_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_ncrgeneration fracas_ncrgeneration_rootcause_id_id_80ebc6f4_fk_fracas_ro; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_ncrgeneration
    ADD CONSTRAINT fracas_ncrgeneration_rootcause_id_id_80ebc6f4_fk_fracas_ro FOREIGN KEY (rootcause_id_id) REFERENCES public.fracas_rootcause(root_cause_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_pbsmaster fracas_pbsmaster_project_id_967c21df_fk_fracas_pr; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_pbsmaster
    ADD CONSTRAINT fracas_pbsmaster_project_id_967c21df_fk_fracas_pr FOREIGN KEY (project_id) REFERENCES public.fracas_product(product_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_eirgeneration fracas_rirgeneration_failure_id_id_392ffa12_fk_fracas_fa; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_eirgeneration
    ADD CONSTRAINT fracas_rirgeneration_failure_id_id_392ffa12_fk_fracas_fa FOREIGN KEY (failure_id_id) REFERENCES public.fracas_failuredata(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_rootcause fracas_rootcause_defect_id_d3f53143_fk_fracas_defect_defect_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_rootcause
    ADD CONSTRAINT fracas_rootcause_defect_id_d3f53143_fk_fracas_defect_defect_id FOREIGN KEY (defect_id) REFERENCES public.fracas_defect(defect_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_systems fracas_systems_project_id_6f83b733_fk_fracas_product_product_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_systems
    ADD CONSTRAINT fracas_systems_project_id_6f83b733_fk_fracas_product_product_id FOREIGN KEY (project_id) REFERENCES public.fracas_product(product_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_userprofile fracas_userprofile_product_id_id_b5877d4c_fk_fracas_pr; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_userprofile
    ADD CONSTRAINT fracas_userprofile_product_id_id_b5877d4c_fk_fracas_pr FOREIGN KEY (product_id_id) REFERENCES public.fracas_product(product_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_userprofile fracas_userprofile_user_id_a6d557eb_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_userprofile
    ADD CONSTRAINT fracas_userprofile_user_id_a6d557eb_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_userprofile fracas_userprofile_user_role_id_9082133f_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_userprofile
    ADD CONSTRAINT fracas_userprofile_user_role_id_9082133f_fk_auth_group_id FOREIGN KEY (user_role_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fracas_userresetkey fracas_userresetkey_user_id_499fbb9d_fk_fracas_userprofile_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fracas_userresetkey
    ADD CONSTRAINT fracas_userresetkey_user_id_499fbb9d_fk_fracas_userprofile_id FOREIGN KEY (user_id) REFERENCES public.fracas_userprofile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

