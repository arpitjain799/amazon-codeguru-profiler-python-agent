import json

from codeguru_profiler_agent.agent_metadata.agent_debug_info import ErrorsMetadata, AgentDebugInfo


class TestAgentDebugInfo:
    class TestAgentDebugInfo:
        def test_it_returns_json_with_error_counts(self):
            errors_metadata = ErrorsMetadata()
            errors_metadata.record_sdk_error("createProfilingGroupErrors")
            subject = AgentDebugInfo(errors_metadata)

            assert subject.serialize_to_json() == {
                "errorsCount": {
                    "configureAgentErrors": 0,
                    "configureAgentRnfeAutoCreateEnabledErrors": 0,
                    "createProfilingGroupErrors": 1,
                    "errorsCount": 1,
                    "postAgentProfileErrors": 0,
                    "postAgentProfileRnfeAutoCreateEnabledErrors": 0,
                    "sdkClientErrors": 1
                }
            }

    class TestErrorsMetadata:
        class TestSerializeToJson:
            def test_it_returns_json_with_error_counts(self):
                subject = ErrorsMetadata()
                subject.record_sdk_error("configureAgentErrors")

                assert subject.serialize_to_json() == {
                    "errorsCount": 1,
                    "sdkClientErrors": 1,
                    "configureAgentErrors": 1,
                    "configureAgentRnfeAutoCreateEnabledErrors": 0,
                    "createProfilingGroupErrors": 0,
                    "postAgentProfileErrors": 0,
                    "postAgentProfileRnfeAutoCreateEnabledErrors": 0
                }

        class TestRecordSdkError:
            def test_it_increments_error_count_when_configureAgentErrors(self):
                subject = ErrorsMetadata()
                subject.record_sdk_error("configureAgentErrors")

                assert subject.errors_count == 1
                assert subject.sdk_client_errors == 1
                assert subject.configure_agent_errors == 1
                assert subject.configure_agent_rnfe_auto_create_enabled_errors == 0
                assert subject.create_profiling_group_errors == 0
                assert subject.post_agent_profile_errors == 0
                assert subject.post_agent_profile_rnfe_auto_create_enabled_errors == 0

            def test_it_increments_error_count_when_configureAgentRnfeAutoCreateEnabledErrors(self):
                subject = ErrorsMetadata()
                subject.record_sdk_error("configureAgentRnfeAutoCreateEnabledErrors")

                assert subject.errors_count == 1
                assert subject.sdk_client_errors == 1
                assert subject.configure_agent_errors == 0
                assert subject.configure_agent_rnfe_auto_create_enabled_errors == 1
                assert subject.create_profiling_group_errors == 0
                assert subject.post_agent_profile_errors == 0
                assert subject.post_agent_profile_rnfe_auto_create_enabled_errors == 0

            def test_it_increments_error_count_when_createProfilingGroupErrors(self):
                subject = ErrorsMetadata()
                subject.record_sdk_error("createProfilingGroupErrors")

                assert subject.errors_count == 1
                assert subject.sdk_client_errors == 1
                assert subject.configure_agent_errors == 0
                assert subject.configure_agent_rnfe_auto_create_enabled_errors == 0
                assert subject.create_profiling_group_errors == 1
                assert subject.post_agent_profile_errors == 0
                assert subject.post_agent_profile_rnfe_auto_create_enabled_errors == 0

            def test_it_increments_error_count_when_postAgentProfileErrors(self):
                subject = ErrorsMetadata()
                subject.record_sdk_error("postAgentProfileErrors")

                assert subject.errors_count == 1
                assert subject.sdk_client_errors == 1
                assert subject.configure_agent_errors == 0
                assert subject.configure_agent_rnfe_auto_create_enabled_errors == 0
                assert subject.create_profiling_group_errors == 0
                assert subject.post_agent_profile_errors == 1
                assert subject.post_agent_profile_rnfe_auto_create_enabled_errors == 0

            def test_it_increments_error_count_when_postAgentProfileRnfeAutoCreateEnabledErrors(self):
                subject = ErrorsMetadata()
                subject.record_sdk_error("postAgentProfileRnfeAutoCreateEnabledErrors")

                assert subject.errors_count == 1
                assert subject.sdk_client_errors == 1
                assert subject.configure_agent_errors == 0
                assert subject.configure_agent_rnfe_auto_create_enabled_errors == 0
                assert subject.create_profiling_group_errors == 0
                assert subject.post_agent_profile_errors == 0
                assert subject.post_agent_profile_rnfe_auto_create_enabled_errors == 1

            def test_it_increments_error_count_when_multiple_errors(self):
                subject = ErrorsMetadata()
                subject.record_sdk_error("createProfilingGroupErrors")
                subject.record_sdk_error("postAgentProfileRnfeAutoCreateEnabledErrors")

                assert subject.errors_count == 2
                assert subject.sdk_client_errors == 2
                assert subject.configure_agent_errors == 0
                assert subject.configure_agent_rnfe_auto_create_enabled_errors == 0
                assert subject.create_profiling_group_errors == 1
                assert subject.post_agent_profile_errors == 0
                assert subject.post_agent_profile_rnfe_auto_create_enabled_errors == 1

            def test_it_resets_error_count(self):
                subject = ErrorsMetadata()
                subject.record_sdk_error("createProfilingGroupErrors")

                assert subject.errors_count == 1
                assert subject.sdk_client_errors == 1
                assert subject.configure_agent_errors == 0
                assert subject.configure_agent_rnfe_auto_create_enabled_errors == 0
                assert subject.create_profiling_group_errors == 1
                assert subject.post_agent_profile_errors == 0
                assert subject.post_agent_profile_rnfe_auto_create_enabled_errors == 0

                subject.reset()

                assert subject.errors_count == 0
                assert subject.sdk_client_errors == 0
                assert subject.configure_agent_errors == 0
                assert subject.configure_agent_rnfe_auto_create_enabled_errors == 0
                assert subject.create_profiling_group_errors == 0
                assert subject.post_agent_profile_errors == 0
                assert subject.post_agent_profile_rnfe_auto_create_enabled_errors == 0
